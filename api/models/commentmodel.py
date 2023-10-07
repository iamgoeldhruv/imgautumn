from django.db import models
from .usermodel import User
from .carddetailsmodel import CardDetails

class Comment(models.Model):
    card = models.ForeignKey(CardDetails, on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on Card NAME {self.card.card_name}'
    