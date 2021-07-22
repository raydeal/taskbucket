from django.contrib import admin

from .models import Location, UserTask


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["name", "country_code", "state_code", "longitude", "latitude", "created", "modified"]


@admin.register(UserTask)
class UserTaskAdmin(admin.ModelAdmin):
    list_display = ["title", "user", "location", "status", "created", "modified"]
