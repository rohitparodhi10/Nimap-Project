from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()
    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by', 'updated_at']
    
    def get_created_by(self,obj):
        return obj.created_by.username    

class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)  # Display user details instead of IDs
    created_by = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']
    
    def get_created_by(self,obj):
        return obj.created_by.username if obj.created_by else None    
