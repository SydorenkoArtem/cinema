import datetime

from django import forms
from django.core.exceptions import ValidationError

from schedule.models import Ticket, Schedule, Hall
from schedule.services import get_free_places_in_hall


class TicketForm(forms.ModelForm):
    """Ticket form implementation"""

    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        self.fields['schedule'].queryset = Schedule.objects.filter(date_show=datetime.datetime.today()).filter(
            start_time__gte=datetime.datetime.now())

    class Meta:
        model = Ticket
        fields = ["quantity", "schedule"]

    def clean(self):
        super(TicketForm, self).clean()
        quantity = self.cleaned_data.get("quantity")
        schedule = self.cleaned_data.get("schedule")
        free_places = get_free_places_in_hall(schedule)

        if quantity > free_places:
            raise ValidationError(f"This quantity is not in stock {free_places}")
        if quantity <= 0:
            raise ValidationError("You have selected the wrong number of tickets. Enter a quantity from 1")


class ScheduleForm(forms.ModelForm):
    """Schedule form implementation"""
    start_date = forms.DateField(widget=forms.SelectDateWidget())
    end_date = forms.DateField(widget=forms.SelectDateWidget())
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': 'HH:MM:SS'}),
                                 error_messages={'required': "This field is required."})
    end_time = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': 'HH:MM:SS'}),
                               error_messages={'required': "This field is required."})

    class Meta:
        model = Schedule
        exclude = ['date_show']

    def clean(self):
        super(ScheduleForm, self).clean()
        start_time = self.cleaned_data['start_time']
        end_time = self.cleaned_data['end_time']
        start_date = self.cleaned_data['start_date']
        end_date = self.cleaned_data['end_date']
        hall = self.cleaned_data['hall']
        price = self.cleaned_data['price']
        all_schedule = Schedule.objects.filter(hall=hall)
        date_today = datetime.date.today()
        for schedule in all_schedule:
            if schedule.start_time <= start_time <= schedule.end_time and \
                    schedule.start_date <= start_date <= schedule.end_date or \
                    schedule.start_time <= end_time <= schedule.end_time and \
                    schedule.start_date <= end_date <= schedule.end_date:
                raise ValidationError("This schedule book yet. Choose other time and date")
            if start_date > end_date or start_date < date_today:
                raise ValidationError("you have chosen the wrong dates")
            if start_time > end_time:
                raise ValidationError("you have chosen the wrong time")
            if price <= 0:
                raise ValidationError("Enter a price more then 0")


class HallForm(forms.ModelForm):
    """Hall form implementation"""

    class Meta:
        model = Hall
        fields = '__all__'
