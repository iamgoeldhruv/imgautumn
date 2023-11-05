from django.shortcuts import render
from api import models
from django.shortcuts import redirect
from django.urls import reverse
import requests
from django.http import request
from api import serializers
from rest_framework import generics,permissions


from rest_framework.views import APIView
from rest_framework.response import Response
from backend import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponse, HttpResponseRedirect
import requests
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token





class ProjectList(generics.ListCreateAPIView):
     queryset = models.Project.objects.all()
     serializer_class = serializers.ProjectSerializer
     authentication_classes=[TokenAuthentication]
     permission_classes=[IsAuthenticated]


class ProjectDetailView(generics.RetrieveAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectDetailsSerializer
    lookup_field = 'project_id'
  
    

class UserProjectListView(generics.ListAPIView):
    serializer_class=serializers.ProjectDetailsSerializer
   
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return models.Project.objects.filter(creator_id=user_id)
    
class CreateProjectView(generics.CreateAPIView):
    serializer_class = serializers.CreateProjectSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        project_name = request.data.get('name')
        existing_project = models.Project.objects.filter(name=project_name).first()

        if existing_project:
            return 
        return super(CreateProjectView, self).create(request, *args, **kwargs)

    def perform_create(self, serializer):
     
        serializer.save(creator=self.request.user)