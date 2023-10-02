from django.db import models

from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    # Additional fields
    user_id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=10, choices=[('member', 'Member'), ('admin', 'Admin')], default='member')
    year = models.PositiveIntegerField()
    profile_pic = models.ImageField(upload_to='profile_pics/')

    def __str__(self):
        return self.username


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

    def __str__(self):
        return self.name



class ProjectMembers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey('Project', to_field='project_id', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} in Project {self.project.project_id}'


class Lists(models.Model):
    list_id = models.AutoField(primary_key=True)
    list_name = models.CharField(max_length=255)
    project = models.ForeignKey('Project',to_field='project_id', on_delete=models.CASCADE)

    def __str__(self):
        return self.list_name

