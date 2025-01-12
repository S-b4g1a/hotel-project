from django.urls import path
from . import views

urlpatterns = [
    path('hotel_list', views.HotelList, name='Hotel List'),
    path('hotel_list_staff', views.HotelListStaff, name='Hotel List Staff'),
    path('hotel_details/<str:hotel_id>/', views.HotelDetails, name='Hotel Details'),
    path('hotel_details_staff/<str:hotel_id>/', views.HotelDetailsStaff, name='Hotel Details Staff'),
    path('hotel_add', views.HotelAdd, name="Hotel Add"),
    path('hotel_delete/<str:hotel_id>', views.HotelDelete, name="Hotel Delete"),
    path('room_add/<str:hotel_id>', views.RoomAdd, name="Room Add"),
    path('room_delete/<str:room_id>', views.RoomDelete, name="Room Delete"),
]