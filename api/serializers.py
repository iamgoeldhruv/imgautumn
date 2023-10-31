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

class ProjectDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields =  '__all__'



