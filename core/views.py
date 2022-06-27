from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, ListAPIView, UpdateAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from .models import Status, Command
from gardens.models import Garden
from .serializers import StatusSerializer, StatusUpdateSerializer, CommandCreateSerializer, CommandRetrieveUpdateSerializer


# Create your views here.
class StatusAPIView(RetrieveAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class StatusUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusUpdateSerializer

    def get_object(self):
        return self.queryset.get(profile_id=self.kwargs.get('pk'))


class CommandCreateListAPIView(ListCreateAPIView):
    queryset = Command.objects.filter(is_done=False)
    serializer_class = CommandCreateSerializer

    def get_object(self):
        return self.queryset.filter(profile_id=self.kwargs.get('pk'))

    def perform_create(self, serializer):
        if serializer.validated_data['command'] == 'water':
            garden = Garden.objects.get(pk=3)
            garden.is_water = 1
            garden.save()
        return serializer.save(profile_id=self.kwargs.get('pk'))


class CommandRetrieveUpdateAPIViewView(RetrieveUpdateAPIView):
    queryset = Command.objects.all()
    serializer_class = CommandRetrieveUpdateSerializer

    def get_object(self):
        return self.queryset.get(profile_id=self.kwargs.get('pk'))


class FinishCommandAPIView(APIView):
    def post(self, request, pk):
        queryset = Command.objects.get(pk=pk)
        queryset.is_done = True
        queryset.save()
        serializer = CommandCreateSerializer(queryset)
        return Response(serializer.data)


class FinishWaterCommandAPIView(APIView):
    def post(self, request, pk):
        queryset = Command.objects.get(pk=pk)
        garden = Garden.objects.get(profile_id=1, section=2)
        garden.is_temi_ready = 1
        garden.save()
        serializer = CommandCreateSerializer(queryset)
        return Response(serializer.data)
