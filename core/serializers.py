from rest_framework import serializers
from .models import Status, Command


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['temperature', 'humidity', 'co2']


class StatusUpdateSerializer(serializers.ModelSerializer):
    illuminance = serializers.FloatField(allow_null=False)
    temperature = serializers.FloatField(allow_null=False)
    humidity = serializers.FloatField(allow_null=False)
    co2 = serializers.FloatField(allow_null=False)

    class Meta:
        model = Status
        fields = ['illuminance', 'temperature', 'humidity', 'co2']
        extra_kwargs = {'illuminance': {'required': False}, 'temperature': {'required': False},
                        'humidity': {'required': False}, 'co2': {'required': False}}


class CommandCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = ['profile_id', 'location', 'command', 'is_done']


class CommandRetrieveUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = ['profile_id', 'location', 'command', 'is_done']
