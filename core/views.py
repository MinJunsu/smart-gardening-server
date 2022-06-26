from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from .models import Status, Command
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
    queryset = Command.objects.all()
    serializer_class = CommandCreateSerializer

    def get_object(self):
        return self.queryset.filter(profile_id=self.kwargs.get('pk'), is_done=False)

    def perform_create(self, serializer):
        serializer.save(profile_id=self.kwargs.get('pk'))


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

