from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from Hotels.models import Hotel, Room
from Bookings.models import Booking

def Homepage(request):
    template = loader.get_template("homepage.html")
    context = {}

    if request.user.is_authenticated:
        bookings = Booking.objects.filter(user_id = request.user.id).values()
        bookings_info = []

        for booking in bookings:
            booking_info = {}
            room_id = booking['room_id']
            room_obj = Room.objects.filter(id=room_id).values()[0]

            hotel_id = room_obj['hotel_id']
            hotel_obj = Hotel.objects.filter(id=hotel_id).values()[0]

            booking_info['id'] = booking['id']
            booking_info['room_designation'] = room_obj['room_designation']
            booking_info['hotel_name'] = hotel_obj['name']
            booking_info['check_in'] = booking['check_in']
            booking_info['check_out'] = booking['check_out']
            booking_info['total_price'] = booking['total_price']

            bookings_info.append(booking_info)

        context['bookings'] = bookings_info

    return HttpResponse(template.render(context, request))