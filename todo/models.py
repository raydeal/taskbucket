from django.db import models
from django.conf import settings

from model_utils.models import TimeStampedModel


class Location(TimeStampedModel):
    name = models.CharField(max_length=100)
    state_code = models.CharField(max_length=100, null=True, blank=True)
    country_code = models.CharField(max_length=2)
    longitude = models.DecimalField(max_digits=10,decimal_places=7)
    latitude = models.DecimalField(max_digits=9,decimal_places=7)

    def __str__(self):
        country_state = self.country_code
        if self.state_code:
            country_state = f"{self.country_code}-{self.state_code}"

        return f"{country_state} {self.name}"


class UserTask(TimeStampedModel):
    NEW = 'new'
    PENDING = 'pending'
    DONE = 'done'
    STATUS_CHOICES = ((NEW, 'New'),
        (PENDING, 'Pending'),
        (DONE, 'Done'))

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    status = models.CharField(max_length=20,default=NEW,choices=STATUS_CHOICES)
    title = models.CharField(max_length=500)
    description = models.TextField(null=True,blank=True)

