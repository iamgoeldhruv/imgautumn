
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
from api.permissions import IsProjectMemberPermission 


class CardDetailsInListView(generics.ListAPIView):
    serializer_class=serializers.CardDetailsSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated,IsProjectMemberPermission]

    def get_queryset(self):
        list_id=self.kwargs['list_id']
        queryset=models.CardDetails.objects.filter(list_id=list_id)
        return queryset


class CreateCardDetailsView(generics.CreateAPIView):
    queryset = models.CardDetails.objects.all()
    serializer_class = serializers.CardDetailsSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()