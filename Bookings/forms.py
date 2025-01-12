from django import forms
import datetime
from dateutil.relativedelta import relativedelta

class BookingCreateForm(forms.Form):
    min_date_in = datetime.datetime.today()
    min_date_out = min_date_in + relativedelta(days=1)

    check_in = forms.DateField(widget = forms.DateInput(attrs={"type":"date","min":min_date_in}))
    check_out = forms.DateField(widget = forms.DateInput(attrs={"type":"date","min":min_date_out}))