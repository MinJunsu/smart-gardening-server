from rest_framework import serializers
from .models import Flower


class FlowerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = ['id', 'name', 'content', 'main_image']


class FlowerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = '__all__'
