# Generated by Django 4.0.4 on 2022-06-26 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gardens', '0004_garden_is_temi_ready'),
    ]

    operations = [
        migrations.AddField(
            model_name='garden',
            name='is_water',
            field=models.BooleanField(default=False),
        ),
    ]