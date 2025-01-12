from django import forms

class HotelAddForm(forms.Form):
    name = forms.CharField()
    address_line_1 = forms.CharField()
    address_line_2 = forms.CharField()
    town_city = forms.CharField()
    country = forms.CharField()
    description = forms.CharField()


class RoomAddForm(forms.Form):
    designation = forms.CharField()
    beds = forms.CharField()
    features = forms.CharField()
    price_per_night = forms.DecimalField(decimal_places=2)
    description = forms.CharField()