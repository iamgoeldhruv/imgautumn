from django.db import models

from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    # Additional fields
    user_id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=10, choices=[('member', 'Member'), ('admin', 'Admin')], default='member')
    year = models.PositiveIntegerField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/',blank=True, null=True)

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



class CardDetails(models.Model):
    list_id = models.ForeignKey('Lists', on_delete=models.CASCADE)
    card_name = models.CharField(max_length=255)
    description = models.TextField()
    assignee = models.ManyToManyField(User, related_name='assigned_cards')
    date_of_creation = models.DateField()
    deadline = models.DateField()
    priority = models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')])
    attachments = models.ImageField(upload_to='card_attachments/', blank=True, null=True)
    color = models.CharField(max_length=7, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Set color to None if attachments is not null
        if self.attachments:
            self.color = None
        super(CardDetails, self).save(*args, **kwargs)

    def __str__(self):
        return self.card_name

class SubCard(models.Model):
    card_id = models.ForeignKey(CardDetails, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    checkbox = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Comment(models.Model):
    card = models.ForeignKey(CardDetails, on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on Card {self.card.name}'

