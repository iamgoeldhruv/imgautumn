from django.shortcuts import render
from .import serializers
from rest_framework import generics,permissions
from . import models
from django.shortcuts import redirect
from django.urls import reverse
import requests
from django.http import request


from rest_framework.views import APIView
from rest_framework.response import Response
from backend import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponse, HttpResponseRedirect
import requests
# Create your views here.
class OAuthAuthorizeView(APIView):
    def get(self, request):
       
        state = 'success'
        print(settings.OAUTH2_CLIENT_ID)


        # Build the authorization URL
        authorization_url = f'https://channeli.in/oauth/authorise/?client_id={settings.OAUTH2_CLIENT_ID}&redirect_uri={settings.OAUTH2_REDIRECT_URI}&state={state}'
        print(authorization_url)
       
       
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
            username=user_data['username']
            name=user_data['person']['fullName']
            words = name.split()
            email=user_data['contactInformation']['emailAddress']
            year=user_data['student']['currentYear']
            profile_pic=user_data['person']['displayPicture']
            print(email)
            print(words[0])
            print(words[1])
            
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
                
                

            return Response({'message': 'User data retrieved successfully', 'data': user_data})
        else:
           
            return Response({'error': 'Failed to retrieve user data'}, status=response.status_code)




    
        
   



class UserList(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    # permission_classes=[permissions.IsAuthenticated]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserDetailsSerializer
    lookup_field = 'user_id'



class ProjectList(generics.ListCreateAPIView):
     queryset = models.Project.objects.all()
     serializer_class = serializers.ProjectSerializer



class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectDetailsSerializer
    lookup_field = 'project_id'

class UserProjectListView(generics.ListAPIView):
    serializer_class=serializers.ProjectDetailsSerializer
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return models.Project.objects.filter(creator_id=user_id)
    
