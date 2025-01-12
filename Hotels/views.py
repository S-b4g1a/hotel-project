from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from django.contrib.admin.views.decorators import staff_member_required

from Hotels.models import Hotel, Room
from Hotels.forms import HotelAddForm, RoomAddForm

def HotelList(request):
    template = loader.get_template("hotel_list.html")
    context = {'hotels': Hotel.objects.all().values()}
    return HttpResponse(template.render(context, request))


def HotelDetails(request, hotel_id):
    template = loader.get_template("hotel_details.html")
    context = {'details': Hotel.objects.filter(id=hotel_id).values()[0],
              'rooms': Room.objects.filter(hotel_id=hotel_id).values()}
    return HttpResponse(template.render(context, request))


@staff_member_required(login_url="/account/sign_in")
def HotelListStaff(request):
    template = loader.get_template("hotel_list_staff.html")
    context = {'hotels': Hotel.objects.all().values()}
    return HttpResponse(template.render(context, request))


@staff_member_required(login_url="/account/sign_in")
def HotelAdd(request):
    template = loader.get_template("hotel_add.html")
    context = {'form': HotelAddForm()}

    if request.method == "POST":
        form = HotelAddForm(request.POST)

        if not form.is_valid():
            context["page_state"] = 2
            return HttpResponse(template.render(context, request))
        
        data = form.cleaned_data
        hotel = Hotel(name=data['name'], address_line_1=data['address_line_1'], address_line_2=data['address_line_2'], town_city=data['town_city'], country=data['country'], description=data['description']) 
        hotel.save()
        
    return HttpResponse(template.render(context, request))


@staff_member_required(login_url="/account/sign_in")
def HotelDelete(request, hotel_id):
    template = loader.get_template("hotel_delete.html")
    context = {}
    if request.method == "POST":
        Hotel.objects.filter(id=hotel_id).delete()
        return redirect('/hotel_list_staff')
    return HttpResponse(template.render(context, request))


@staff_member_required(login_url="/account/sign_in")
def HotelDetailsStaff(request, hotel_id):
    template = loader.get_template("hotel_details_staff.html")
    context = {'rooms': Room.objects.filter(hotel_id=hotel_id).values(),
               'hotel_details': Hotel.objects.filter(id=hotel_id).values()[0],}
    return HttpResponse(template.render(context, request))


@staff_member_required(login_url="/account/sign_in")
def RoomAdd(request, hotel_id):
    template = loader.get_template("room_add.html")
    context = {'form': RoomAddForm(),
               'hotel_name': Hotel.objects.filter(id=hotel_id).values()[0]['name'],}

    if request.method == "POST":
        form = RoomAddForm(request.POST)

        if not form.is_valid():
            context["page_state"] = 2
            return HttpResponse(template.render(context, request))
        
        data = form.cleaned_data
        room = Room(room_designation=data['designation'], room_beds=data['beds'], room_features=data['features'], price_per_night=data['price_per_night'], description=data['description'], availability=True, hotel_id=hotel_id) 
        room.save()
        
    return HttpResponse(template.render(context, request))


@staff_member_required(login_url="/account/sign_in")
def RoomDelete(request, room_id):
    template = loader.get_template("room_delete.html")
    context = {}
    if request.method == "POST":
        Room.objects.filter(id=room_id).delete()
        return redirect('/hotel_list_staff')
    return HttpResponse(template.render(context, request))