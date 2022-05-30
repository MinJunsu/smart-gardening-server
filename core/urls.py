from django.urls import path
from .views import StatusAPIView


urlpatterns = [
    path('<int:pk>/', StatusAPIView.as_view())
]
