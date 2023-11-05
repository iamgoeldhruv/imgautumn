from rest_framework import serializers
from .import models
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('user_id', 'username', 'role', 'year', 'profile_pic')

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



