from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Garden, Diary
from .serializers import GardenLightUpdateSerializer, GardenUpdateSerializer, GardenListSerializer, GardenDetailSerializer, DiaryListSerializer, DiaryCreateSerializer, GardenWaterUpdateSerializer


# Create your views here.
class GardenHumidityUpdateView(UpdateAPIView):
    queryset = Garden.objects.all()
    serializer_class = GardenUpdateSerializer

    def get_object(self):
        print(self.kwargs)
        return self.queryset.get(profile_id=self.kwargs.get('pk'), section=self.kwargs.get('section'))


class GardenWaterUpdateView(RetrieveUpdateAPIView):
    queryset = Garden.objects.all()
    serializer_class = GardenWaterUpdateSerializer

    def get_object(self):
        return self.queryset.get(profile_id=self.kwargs.get('pk'), section=self.kwargs.get('section'))


class GardenLightUpdateView(RetrieveUpdateAPIView):
    queryset = Garden.objects.all()
    serializer_class = GardenLightUpdateSerializer

    def get_object(self):
        return self.queryset.get(profile_id=self.kwargs.get('pk'), section=1)


class GardenListAPIView(ListAPIView):
    queryset = Garden.objects.all()
    serializer_class = GardenListSerializer
    # permission_classes = [IsAuthenticated]


class GardenRetrieveAPIView(RetrieveAPIView):
    queryset = Garden.objects.all()
    serializer_class = GardenDetailSerializer


class GardenDiaryListAPIView(ListAPIView):
    queryset = Diary.objects.all().order_by('created_at')
    serializer_class = DiaryListSerializer
    lookup_field = ['garden']


class DiaryCreateAPIView(CreateAPIView):
    serializer_class = DiaryCreateSerializer
    queryset = Diary.objects.all()

    def perform_create(self, serializer):
        return serializer.save(garden_id=self.kwargs.get('pk'))
