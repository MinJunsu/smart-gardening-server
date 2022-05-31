from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from .models import Status
from .serializers import StatusSerializer, StatusUpdateSerializer


# Create your views here.
class StatusAPIView(RetrieveAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class StatusUpdateAPIView(UpdateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusUpdateSerializer

    def get_object(self):
        return self.queryset.get(profile_id=self.kwargs.get('pk'))
