from django.urls import path
from .views import StatusAPIView, StatusUpdateAPIView, CommandCreateListAPIView, FinishCommandAPIView


urlpatterns = [
    path('<int:pk>/', StatusAPIView.as_view()),
    path('<int:pk>/update/', StatusUpdateAPIView.as_view()),
    path('<int:pk>/command/', CommandCreateListAPIView.as_view()),
    path('command/<int:pk>/done/', FinishCommandAPIView.as_view()),
]
