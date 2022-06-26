from django.urls import path
from .views import GardenLightUpdateView, GardenHumidityUpdateView, GardenListAPIView, GardenRetrieveAPIView, GardenDiaryListAPIView, DiaryCreateAPIView, GardenWaterUpdateView


urlpatterns = [
    path('', GardenListAPIView.as_view(), name='garden-list'),
    path('<int:pk>/water/<int:section>/', GardenWaterUpdateView.as_view()),
    path('<int:pk>/light/<int:section>/', GardenLightUpdateView.as_view()),
    path('<int:pk>/humidity/<int:section>/update/', GardenHumidityUpdateView.as_view()),
    path('<int:pk>/', GardenRetrieveAPIView.as_view(), name='garden-list'),
    path('<int:pk>/diary/', GardenDiaryListAPIView.as_view(), name='diary-list'),
    path('<int:pk>/diary/create', DiaryCreateAPIView.as_view(), name='diary-create')
]
