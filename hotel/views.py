from rest_framework import generics

from hotel.models import Hotel, Meal
from hotel.serializers import HotelSerializer, MealSerializer


class HotelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class HotelViewList(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class MealView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class MealViewAllAndCreate(generics.ListCreateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

