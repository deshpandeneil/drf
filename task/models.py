from django.db import models


# Create your models here.

class Record(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
