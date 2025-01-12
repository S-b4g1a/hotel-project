from django.urls import path
from . import views

urlpatterns = [
    path('booking_create/<str:hotel_id>/<str:room_id>', views.BookingCreate, name='Create Booking'),
    path('booking_delete/<str:booking_id>', views.BookingDelete, name='Delete Booking'),
]