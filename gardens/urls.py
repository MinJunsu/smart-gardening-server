from django.urls import path
from .views import GardenListAPIView, GardenRetrieveAPIView, GardenDiaryListAPIView, DiaryCreateAPIView


urlpatterns = [
    path('', GardenListAPIView.as_view(), name='garden-list'),
    path('<int:pk>/', GardenRetrieveAPIView.as_view(), name='garden-list'),
    path('<int:pk>/diary/', GardenDiaryListAPIView.as_view(), name='diary-list'),
    path('<int:pk>/diary/create', DiaryCreateAPIView.as_view(), name='diary-create')
]