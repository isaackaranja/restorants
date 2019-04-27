from django.contrib import admin


from hotel.models import Hotel, Meal, Room, Accommodation


@admin.register(Meal, Hotel, Room, Accommodation)
class MealAdmin(admin.ModelAdmin):
    pass
