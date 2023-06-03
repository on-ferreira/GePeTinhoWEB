from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    #user = pegar current user

    class Meta:
        ordering = ('created_at', )

    def __str__(self):
        return str(self.pk)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.TextField(max_length=10)
    content = models.TextField()
    typeofMessage = models.TextField(default='text')

    class Meta:
        ordering = ('created_at', )

    def __str__(self):
        return self.content
