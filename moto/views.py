from rest_framework import generics
from .models import Moto
from .serializers import MotoSerializer
from .permissions import IsOwnerOrReadOnly


class MotoList(generics.ListCreateAPIView):
    queryset = Moto.objects.all()  # when you call the API, you will get all of the motos
    serializer_class = MotoSerializer


class MotoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer
    permission_classes = (IsOwnerOrReadOnly,)
