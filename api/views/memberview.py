# myapp/views.py
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from api import serializers
from api import models
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class ProjectMembersCreateView(generics.CreateAPIView):
    queryset = models.ProjectMembers.objects.all()
    serializer_class = serializers.ProjectMembersSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]


    def create(self, request, *args, **kwargs):
        user_id = request.data.get('user')
        project_id = request.data.get('project')
        existing_member=models.ProjectMembers.objects.filter(user=user_id,project=project_id).exists()
        if(existing_member):
           
            
            return Response( status=status.HTTP_400_BAD_REQUEST)
     
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class ProjectMembersListView(generics.ListAPIView):
    serializer_class = serializers.ViewProjectMembersSerializer

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return models.ProjectMembers.objects.filter(project=project_id)
    

class UserProjectsView(generics.ListAPIView):
    def get(self, request, user_id, format=None):
        try:
            projects = models.ProjectMembers.objects.filter(user_id=user_id)
            serializer = serializers.ProjectMembers1Serializer(projects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except models.ProjectMembers.DoesNotExist:
            return Response({"message": "User not found or not a member of any projects"}, status=status.HTTP_404_NOT_FOUND)


