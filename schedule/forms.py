from django import forms

from schedule.models import Ticket, Schedule, Hall


class TicketForm(forms.ModelForm):
    """Ticket form implementation"""

    class Meta:
        model = Ticket
        fields = ["quantity", "schedule"]

    # def clean(self):
    #     super(Ticket, self).clean()
    #     quantity = self.cleaned_data.get("quantity")
    #     product = self.cleaned_data.get("product")
    #     amount_product = Product.objects.get(product=product).amount
    #
    #     if quantity > amount_product:
    #         raise ValidationError(f"This quantity is not in stock {amount_product}")


class ScheduleForm(forms.ModelForm):
    """Schedule form implementation"""

    class Meta:
        model = Schedule
        exclude = ["date_show"]


class HallForm(forms.ModelForm):
    """Hall form implementation"""

    class Meta:
        model = Hall
        fields = '__all__'
