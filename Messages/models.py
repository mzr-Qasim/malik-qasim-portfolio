from django.db import models

# Create your models here.
from django.db import models


class Messages(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    messagesubject = models.CharField(max_length=60)
    message = models.TextField(max_length=500)
