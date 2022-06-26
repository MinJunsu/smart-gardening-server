from django.urls import path
from .views import StatusAPIView, StatusUpdateAPIView, CommandCreateAPIView, CommandRetrieveUpdateAPIViewView


urlpatterns = [
    path('<int:pk>/', StatusAPIView.as_view()),
    path('<int:pk>/update/', StatusUpdateAPIView.as_view()),
    path('<int:pk>/command/', CommandCreateAPIView.as_view()),
    path('<int:pk>/command/', CommandRetrieveUpdateAPIViewView.as_view()),
]
