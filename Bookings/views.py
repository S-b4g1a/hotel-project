from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth.decorators import login_required

import datetime

from Bookings.forms import BookingCreateForm
from Bookings.models import Booking
from Hotels.models import Hotel, Room


@login_required(login_url='/account/sign_in')
def BookingCreate(request, hotel_id, room_id):
    template = loader.get_template("booking_create.html")
    context = {"hotel": Hotel.objects.filter(id=hotel_id).values()[0],
               "room": Room.objects.filter(id=room_id).values()[0],
               "form": BookingCreateForm()}
    
    if request.method == "POST":
        form = BookingCreateForm(request.POST)

        if not form.is_valid():
            context["page_state"] = 2
            return HttpResponse(template.render(context, request))
        
        data = form.cleaned_data

        if data['check_in'] < datetime.date.today():
            context["page_state"] = 3
            return HttpResponse(template.render(context, request))

        if data['check_out'] < datetime.date.today():
            context["page_state"] = 4
            return HttpResponse(template.render(context, request))
        
        if data['check_out'] < data['check_in']:
            context["page_state"] = 5
            return HttpResponse(template.render(context, request))
        
        total_price = (data['check_out'] - data['check_in']).days * Room.objects.filter(id=room_id).values()[0]['price_per_night']

        booking = Booking(total_price=total_price, check_in=data['check_in'], check_out=data['check_out'], room_id=room_id, user_id=request.user.id, is_confirmed=False, is_cancelled=False, is_historical=False)
        booking.save()

    context["page_state"] = 0    
    return HttpResponse(template.render(context, request))


@login_required(login_url='/account/sign_in')
def BookingDelete(request, booking_id):
    template = loader.get_template("booking_delete.html")
    context = {}
    if request.method == "POST":
        Booking.objects.filter(id=booking_id).delete()
        return redirect('/homepage')
    return HttpResponse(template.render(context, request))
