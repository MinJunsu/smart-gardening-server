from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from .models import Flower
from .serializers import FlowerListSerializer, FlowerDetailSerializer
from .paginations import FlowerPageNumberPagination
# Create your views here.


class FlowerListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = FlowerListSerializer
    pagination_class = FlowerPageNumberPagination

    def get_queryset(self):
        word = self.request.query_params.get('word')
        queryset = Flower.objects.all()
        if word:
            return queryset.filter(name__icontains=word)
        return queryset


class FlowerDetailAPIView(RetrieveAPIView):
    queryset = Flower.objects.all()
    permission_classes = [AllowAny]
    serializer_class = FlowerDetailSerializer
