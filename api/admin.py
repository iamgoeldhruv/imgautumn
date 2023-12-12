from django.contrib import admin
from . import models
from rest_framework.authtoken.models import Token



# Register your models here.

admin.site.register(models.User)
admin.site.register(models.Project)
admin.site.register(models.ProjectMembers)
admin.site.register(models.Lists)
admin.site.register(models.CardDetails)
admin.site.register(models.SubCard)
admin.site.register(models.Comment)
admin.site.register(models.ChatMessage)