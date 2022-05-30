from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from .models import Status
from .serializers import StatusSerializer


# Create your views here.
class StatusAPIView(RetrieveAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
