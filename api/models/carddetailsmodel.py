from django.db import models
from .usermodel import User
from .listmodel import Lists
class CardDetails(models.Model):
    list_id = models.ForeignKey(Lists, on_delete=models.CASCADE)
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