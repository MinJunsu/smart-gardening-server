# Generated by Django 4.0.4 on 2022-05-28 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('month', models.SmallIntegerField()),
                ('day', models.SmallIntegerField()),
                ('flower_language', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=300)),
                ('usage', models.CharField(max_length=300)),
                ('growth', models.CharField(max_length=300)),
                ('main_image', models.URLField()),
            ],
        ),
    ]