from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    client_name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='clients')
    
    def __str__(self) -> str:
        return self.client_name
    

class Project(models.Model):
    project_name=models.CharField(max_length=255)
    client=models.ForeignKey(Client, related_name='projects', on_delete=models.CASCADE)
    users=models.ManyToManyField(User, related_name="projects_user")
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User, on_delete=models.SET_NULL,related_name='created_projects', null=True, blank=True)
    
    def __str__(self) -> str:
        return self.project_name
    
        