from django.urls import path
from .views import StatusAPIView, StatusUpdateAPIView, CommandCreateListAPIView, CommandRetrieveUpdateAPIViewView


urlpatterns = [
    path('<int:pk>/', StatusAPIView.as_view()),
    path('<int:pk>/update/', StatusUpdateAPIView.as_view()),
    path('<int:pk>/command/', CommandCreateListAPIView.as_view()),
    path('<int:pk>/command/<int:id>/', CommandRetrieveUpdateAPIViewView.as_view()),
]
