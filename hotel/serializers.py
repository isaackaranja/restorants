from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from hotel.models import Hotel, Meal, Room, Accommodation


class MealSerializer(ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'


class RoomSerializer(ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'


class HotelSerializer(ModelSerializer):
    meals = MealSerializer(many=True, required=False)
    rooms = RoomSerializer(many=True, required=False)

    class Meta:
        model = Hotel
        fields = '__all__'


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)


class AccommodationSerializer(ModelSerializer):
    user = UserSerializer()
    room = RoomSerializer()

    class Meta:
        model = Accommodation
        fields = '__all__'