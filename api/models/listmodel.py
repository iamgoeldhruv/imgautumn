from django.db import models
from .projectmodel import Project
class Lists(models.Model):
    list_id = models.AutoField(primary_key=True)
    list_name = models.CharField(max_length=255)
    project = models.ForeignKey(Project,to_field='project_id', on_delete=models.CASCADE)

    def __str__(self):
        return self.list_name