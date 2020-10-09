from django.db import models

class Comment(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
