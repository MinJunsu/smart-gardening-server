from django.db import models
from datetime import datetime, timedelta

# Create your models here.


class Garden(models.Model):
    profile = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='%Y/%m/%d')
    section = models.IntegerField()
    name = models.CharField(max_length=10)
    period = models.IntegerField()
    humidity = models.FloatField()
    watering_time = models.DateTimeField()
    is_turn_on = models.IntegerField(default=0)
    is_water = models.IntegerField(default=0)
    is_temi_ready = models.IntegerField(default=0)


class Diary(models.Model):
    garden = models.ForeignKey('gardens.Garden', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='diary/%Y/%m/%d')
    title = models.CharField(max_length=30)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

