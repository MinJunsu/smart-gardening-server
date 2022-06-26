from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, CreateAPIView, RetrieveUpdateAPIView
from .models import Status, Command
from .serializers import StatusSerializer, StatusUpdateSerializer, CommandCreateSerializer, CommandRetrieveUpdateSerializer


# Create your views here.
class StatusAPIView(RetrieveAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class StatusUpdateAPIView(UpdateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusUpdateSerializer

    def get_object(self):
        return self.queryset.get(profile_id=self.kwargs.get('pk'))


class CommandCreateAPIView(CreateAPIView):
    queryset = Command.objects.all()
    serializer_class = CommandCreateSerializer

    def get_object(self):
        return self.queryset.get(profile_id=self.kwargs.get('pk'))


class CommandRetrieveUpdateAPIViewView(RetrieveUpdateAPIView):
    queryset = Command.objects.all()
    serializer_class = CommandRetrieveUpdateSerializer

    def get_object(self):
        return self.queryset.get(profile_id=self.kwargs.get('pk'))
