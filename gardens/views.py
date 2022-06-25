from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Garden, Diary
from .serializers import GardenUpdateSerializer, GardenListSerializer, GardenDetailSerializer, DiaryListSerializer, DiaryCreateSerializer


# Create your views here.
class GardenHumidityUpdateView(UpdateAPIView):
    queryset = Garden.objects.all()
    serializer_class = GardenUpdateSerializer

    def get_object(self):
        print(self.kwargs)
        return self.queryset.get(profile_id=self.kwargs.get('pk'), section=self.kwargs.get('section'))


class GardenListAPIView(ListAPIView):
    queryset = Garden.objects.all()
    serializer_class = GardenListSerializer
    # permission_classes = [IsAuthenticated]


class GardenRetrieveAPIView(RetrieveAPIView):
    queryset = Garden.objects.all()
    serializer_class = GardenDetailSerializer


class GardenDiaryListAPIView(ListAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiaryListSerializer
    lookup_field = ['garden']


class DiaryCreateAPIView(CreateAPIView):
    serializer_class = DiaryCreateSerializer
    queryset = Diary.objects.all()
