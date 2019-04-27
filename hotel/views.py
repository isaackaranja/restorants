from rest_framework import generics

from hotel.models import Hotel
from hotel.serializers import HotelSerializer


class HotelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class HotelViewList(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
