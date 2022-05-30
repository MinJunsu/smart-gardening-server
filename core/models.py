from django.db import models

# Create your models here.


class Status(models.Model):
    profile = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    temperature = models.FloatField()
    humidity = models.FloatField()
    co2 = models.IntegerField()


class Comment(models.Model):
    pass
