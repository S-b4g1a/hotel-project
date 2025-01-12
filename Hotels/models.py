from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address_line_1 = models.TextField()
    address_line_2 = models.TextField()
    town_city = models.TextField()
    country = models.TextField()
    description = models.TextField()

    # image = models.ImageField(upload_to='hotels/')


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_designation = models.TextField()
    room_beds = models.TextField()
    room_features = models.TextField()
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)

    # def __str__(self):
    #     return f"{self.room_type} - {self.hotel.name} (${self.price_per_night}/night)"
