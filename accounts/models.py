from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
