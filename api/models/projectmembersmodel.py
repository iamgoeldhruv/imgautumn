from django.db import models
from .usermodel import User
from .projectmodel import Project
class ProjectMembers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, to_field='project_id', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} in Project {self.project.project_id}'





