from django.db import models

from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    # Additional fields
    nick_name = models.CharField(max_length=255,blank=True, null=True)


    user_id = models.AutoField(primary_key=True)
    


    role = models.CharField(max_length=10, choices=[('member', 'Member'), ('admin', 'Admin')], default='member')
    year = models.PositiveIntegerField(blank=True, null=True)
    profile_pic = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.username