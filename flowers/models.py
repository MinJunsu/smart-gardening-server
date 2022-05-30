from django.db import models

# Create your models here.


class Flower(models.Model):
    name = models.CharField(max_length=100)
    month = models.SmallIntegerField()
    day = models.SmallIntegerField()
    flower_language = models.CharField(max_length=30)
    content = models.CharField(max_length=300)
    usage = models.CharField(max_length=300)
    growth = models.CharField(max_length=300)
    main_image = models.URLField()

    def __str__(self):
        return self.name
