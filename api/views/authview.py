from django.shortcuts import render
from api import models
from django.shortcuts import redirect
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from backend import settings
import requests
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.http import HttpResponseRedirect



# Create your views here.
class OAuthAuthorizeView(APIView):
    def get(self, request):
       
        state = 'success'
        print(settings.OAUTH2_CLIENT_ID)
        authorization_url = f'https://channeli.in/oauth/authorise/?client_id={settings.OAUTH2_CLIENT_ID}&redirect_uri={settings.OAUTH2_REDIRECT_URI}&state={state}'
        
        return redirect(authorization_url)
    


    
class oauth2_callback(APIView):
    def get(self, request):
        code = request.GET.get('code')
        token_url = 'https://channeli.in/open_auth/token/'
        payload = {
            'code': code,
            'client_id': settings.OAUTH2_CLIENT_ID,
            'client_secret': settings.OAUTH2_CLIENT_SECRET,
            'redirect_uri': settings.OAUTH2_REDIRECT_URI,
            'grant_type': 'authorization_code',
        }
        response = requests.post(token_url, data=payload)
        token_data = response.json()
        access_token = token_data.get('access_token')
        if(access_token):
           new_url = f'http://127.0.0.1:8000/get_user_data/?access_token={access_token}'
           return redirect(new_url)
        else:
             return Response({'error': 'Access token not found'})


        
        


class GetUserDataView(APIView):
    def get(self, request):
        access_token = request.GET.get('access_token')  
        if not access_token:
            return Response({'error': 'Access token is missing'}, status=400)

       
        user_data_url = 'https://channeli.in/open_auth/get_user_data/'
        headers = {'Authorization': f'Bearer {access_token}'}

        response = requests.get(user_data_url, headers=headers)

        if response.status_code == 200:

            user_data = response.json()
            # role=user_data['person']['roles'][1]['role']
            role='Maintainer'
            username=user_data['username']
            name=user_data['person']['fullName']
            words = name.split()
            email=user_data['contactInformation']['emailAddress']
            year=user_data['student']['currentYear']
            profile_pic=user_data['person']['displayPicture']
            print(words)
            if(role=='Maintainer'):
           
                
                existing_users = models.User.objects.filter(username=username)
                
                if(not existing_users):
                    new_user=models.User.objects.create(
                        first_name=words[0],
                        last_name=words[1],
                        username=username,
                        email=email,
                        year=year,
                        profile_pic=profile_pic



                    )
                    new_user.save()
                    
                else: 
                    print('user already exist')
                existing_users1 = models.User.objects.get(username=username)
                token,created=Token.objects.get_or_create(user=existing_users1)
                print(token.key)
                authToken=token.key
                userId=existing_users1.user_id
                userName=existing_users1.username
                response = HttpResponseRedirect('http://localhost:3000/?auth_token=' + authToken + '&userid=' + str(userId) + '&username=' + userName)

               
                return response
               
                
            else:
                return HttpResponseRedirect('http://localhost:3000/')
        else:
            
            return HttpResponseRedirect('http://localhost:3000',status==451)
            
            
