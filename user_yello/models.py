from django.db import models

# Create your models here.
class UserAccount(models.Model):
    email = models.CharField(max_length=75, unique=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=1000)
    