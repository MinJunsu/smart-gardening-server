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


class DiaryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ['image', 'title', 'description']


class GardenUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garden
        fields = ['humidity']


class GardenLightUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garden
        fields = ['is_turn_on']


class GardenWaterUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garden
        fields = ['is_water', 'is_temi_ready']
