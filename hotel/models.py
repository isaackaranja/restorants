from django.contrib.auth.models import User
from django.db import models


class Meal(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        app_label = 'hotel'


class Room(models.Model):
    superior_rooms = 'Superior Rooms'
    honey_moon_suites = 'Honey moon suites'
    master = 'Master'
    executive_suite = 'Executive Suite'
    ambassadorial_rooms = 'Ambassadorial Rooms'
    standard_rooms = 'Standard Rooms'

    choices = (
        (honey_moon_suites, honey_moon_suites),
        (master, master),
        (executive_suite, executive_suite),
        (superior_rooms, superior_rooms),
        (ambassadorial_rooms, ambassadorial_rooms),
        (standard_rooms, standard_rooms)
    )
    rating = models.CharField(max_length=100, choices=choices, default=master)
    price = models.IntegerField()
    room_number = models.IntegerField()
    no_bed = models.IntegerField()
    is_booked = models.BooleanField(default=False)

    class Meta:
        app_label = 'hotel'


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    ratings = models.IntegerField()
    meals = models.ManyToManyField(Meal, blank=True, related_name="hotel")
    rooms = models.ManyToManyField(Room, blank=True, related_name='rooms')

    class Meta:
        app_label = 'hotel'


class Accommodation(models.Model):
    user = models.ForeignKey(User, name='user', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, name='room', on_delete=models.CASCADE)
    start_date = models.DateField(auto_created=True)
    end_date = models.DateField()

    class Meta:
        app_label = 'hotel'

