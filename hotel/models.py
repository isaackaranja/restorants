from django.db import models


class Meal(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=1000)


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    ratings = models.IntegerField()
    meals = models.ManyToManyField(Meal)