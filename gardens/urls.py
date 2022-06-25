from django.urls import path
from .views import GardenLightUpdateView, GardenHumidityUpdateView, GardenListAPIView, GardenRetrieveAPIView, GardenDiaryListAPIView, DiaryCreateAPIView


urlpatterns = [
    path('', GardenListAPIView.as_view(), name='garden-list'),
    path('<int:pk>/light/update/<int:section>/', GardenLightUpdateView.as_view()),
    path('<int:pk>/humidity/update/<int:section>/', GardenHumidityUpdateView.as_view()),
    path('<int:pk>/', GardenRetrieveAPIView.as_view(), name='garden-list'),
    path('<int:pk>/diary/', GardenDiaryListAPIView.as_view(), name='diary-list'),
    path('<int:pk>/diary/create', DiaryCreateAPIView.as_view(), name='diary-create')
]
