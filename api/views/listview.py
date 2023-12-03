
from django.shortcuts import render
from api import models
from django.shortcuts import redirect
from django.urls import reverse
import requests
from django.http import request
from api import serializers
from rest_framework import generics,permissions
from rest_framework import status


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


class ListsInProjectView(generics.ListCreateAPIView):
    serializer_class = serializers.ListsSerializer

    def get_queryset(self):
        project_id = self.kwargs.get('project_id')
        return models.Lists.objects.filter(project__project_id=project_id)

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_id')
        project = models.Project.objects.get(project_id=project_id)
        serializer.save(project=project)








