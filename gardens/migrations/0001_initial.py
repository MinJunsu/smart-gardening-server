# Generated by Django 4.0.4 on 2022-05-28 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Garden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.IntegerField()),
                ('name', models.CharField(max_length=10)),
                ('period', models.IntegerField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
        migrations.CreateModel(
            name='GardenManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('humidity', models.FloatField()),
                ('watering_time', models.DateTimeField()),
                ('is_turn_on', models.BooleanField()),
                ('garden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gardens.garden')),
            ],
        ),
    ]