from rest_framework.serializers import ModelSerializer

from hotel.models import Hotel, Meal


class MealSerializer(ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'


class HotelSerializer(ModelSerializer):
    meals = MealSerializer(many=True)

    class Meta:
        model = Hotel
        fields = '__all__'