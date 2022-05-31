from rest_framework import serializers
from .models import Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['temperature', 'humidity', 'co2']


class StatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['illuminance', 'temperature', 'humidity', 'co2']
