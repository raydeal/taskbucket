from django.contrib import admin

from .models import Location, UserTask

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass

@admin.register(UserTask)
class UserTaskAdmin(admin.ModelAdmin):
    pass

