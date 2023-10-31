from django.db import models
from .usermodel import User
class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_creation = models.DateField()
    name = models.CharField(max_length=255)
    wiki = models.CharField(max_length=255)
    description = models.TextField()
    is_visible = models.BooleanField(default=True)
    project_link = models.URLField(max_length=200, blank=True, null=True)
    github_link = models.URLField(max_length=200, blank=True, null=True)
    is_completed = models.BooleanField(default=False) 

    def __str__(self):
        return self.name
    # def creator_name(self):
    #     return self.creator.name