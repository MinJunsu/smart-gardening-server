from django.urls import path
from .views import GardenListAPIView, GardenRetrieveAPIView, GardenDiaryListAPIView


urlpatterns = [
    path('', GardenListAPIView.as_view(), name='garden-list'),
    path('<int:pk>/', GardenRetrieveAPIView.as_view(), name='garden-list'),
    path('<int:pk>/diary/', GardenDiaryListAPIView.as_view(), name='diary-list')
]
