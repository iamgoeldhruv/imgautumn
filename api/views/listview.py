
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



class Listslist(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self, request, project_id):
        lists = models.Lists.objects.filter(project__project_id=project_id)
        serializer = serializers.ListsSerializer(lists, many=True)
        return Response(serializer.data)
    

    def post(self, request, project_id):
        serializer = serializers.ListsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(project_id=project_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class ListsDetail(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self, request, list_id):
        try:
            lists = models.Lists.objects.get(list_id=list_id)
        except models.Lists.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.ListsSerializer(lists)
        return Response(serializer.data)

    def put(self, request, list_id):
        try:
            lists = models.Lists.objects.get(list_id=list_id)
        except models.Lists.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.ListsSerializer(lists, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, list_id):
        try:
            lists = models.Lists.objects.get(list_id=list_id)
        except models.Lists.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        lists.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


