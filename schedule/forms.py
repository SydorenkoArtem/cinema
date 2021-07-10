from django import forms
from django.core.exceptions import ValidationError

from schedule.models import Ticket, Schedule, Hall
from schedule.services import get_free_places_in_hall


class TicketForm(forms.ModelForm):
    """Ticket form implementation"""

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


class ScheduleForm(forms.ModelForm):
    """Schedule form implementation"""

    class Meta:
        model = Schedule
        exclude = ["date_show"]

    def clean(self):
        super(ScheduleForm, self).clean()
        start_time = self.cleaned_data['start_time']
        end_time = self.cleaned_data['end_time']
        start_date = self.cleaned_data['start_date']
        end_date = self.cleaned_data['end_date']
        hall = self.cleaned_data['hall']
        all_schedule = Schedule.objects.filter(hall=hall)
        for schedule in all_schedule:
            if schedule.start_time <= start_time <= schedule.end_time and \
                    schedule.start_date <= start_date <= schedule.end_date or \
                    schedule.start_time <= end_time <= schedule.end_time and \
                    schedule.start_date <= end_date <= schedule.end_date:
                raise ValidationError("This schedule book yet. Choose other time and date")


class HallForm(forms.ModelForm):
    """Hall form implementation"""

    class Meta:
        model = Hall
        fields = '__all__'
