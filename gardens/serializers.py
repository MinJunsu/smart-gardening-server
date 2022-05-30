from rest_framework import serializers
from .models import Garden, Diary


class GardenListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garden
        fields = ['id', 'image', 'section', 'name', 'is_turn_on', 'is_water']


class GardenDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garden
        fields = ['id', 'image', 'section', 'name', 'period', 'humidity', 'is_turn_on', 'is_water']


class DiaryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = '__all__'
