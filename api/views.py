from django.shortcuts import render
from .import serializers
from rest_framework import generics,permissions
from . import models

# Create your views here.
class UserList(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    # permission_classes=[permissions.IsAuthenticated]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserDetailsSerializer
    lookup_field = 'user_id'