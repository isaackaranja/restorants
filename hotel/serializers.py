from rest_framework.serializers import ModelSerializer

from hotel.models import Hotel


class HotelSerializer(ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'
class Mealserializer(ModelSerializer):
    class Meta:
        model = Meal
        field = '__all__'
