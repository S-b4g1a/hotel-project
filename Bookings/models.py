from django.db import models
from django.contrib.auth.models import User

import datetime

from Hotels.models import Room

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.DateField(("Date"), default=datetime.date.today)
    check_out = models.DateField(("Date"), default=datetime.date.today)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    is_confirmed = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)
    is_historical = models.BooleanField(default=True)


    def calculate_total_price(self):
        return self.room.price_per_night * (self.check_out - self.check_in).days
