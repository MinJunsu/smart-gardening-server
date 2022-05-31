from django.urls import path
from .views import StatusAPIView, StatusUpdateAPIView


urlpatterns = [
    path('<int:pk>/', StatusAPIView.as_view()),
    path('<int:pk>/update', StatusUpdateAPIView.as_view())
]
