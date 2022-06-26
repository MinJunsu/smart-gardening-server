from django.db import models

# Create your models here.


class Status(models.Model):
    profile = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    illuminance = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    co2 = models.IntegerField()


class Comment(models.Model):
    pass


class Command(models.Model):
    profile = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    location = models.CharField(max_length=10)
    command = models.CharField(max_length=100)
    command_kor = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
