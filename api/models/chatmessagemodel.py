from django.db import models
from .usermodel import User

class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="user")
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="receiver")

    message = models.TextField()

    is_read = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
