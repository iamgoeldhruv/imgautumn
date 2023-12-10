from rest_framework import serializers
from .import models
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    creator=serializers.CharField(source='creator.username', read_only=True)
    class Meta:
        model = models.Project
        fields = '__all__'


class CreateProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Project
        fields = ('creator','name','description','wiki','github_link','date_of_creation','is_visible')

class ProjectDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields =  '__all__'


class ListsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lists
        fields = '__all__'

class ProjectMembersSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = models.ProjectMembers
        fields = ('user', 'project')





class ListsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lists
        fields = ['list_id', 'list_name', 'project']


class CardDetailsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.CardDetails
        fields = '__all__'




class ViewProjectMembersSerializer(serializers.ModelSerializer):
    user = UserSerializer()  

    class Meta:
        model = models.ProjectMembers
        fields = ['user', 'project']  

class ProjectMembers1Serializer(serializers.ModelSerializer):
    project = ProjectSerializer() 

    class Meta:
        model = models.ProjectMembers
        fields = ['project']