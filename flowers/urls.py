from django.urls import path
from .views import FlowerListAPIView, FlowerDetailAPIView


urlpatterns = [
    path('', FlowerListAPIView.as_view(), name='flower-list'),
    path('<int:pk>/', FlowerDetailAPIView.as_view(), name='flower-detail')
]
