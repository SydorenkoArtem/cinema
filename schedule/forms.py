from django import forms

from schedule.models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["film", "quantity", "schedule"]

    # def clean(self):
    #     super(Ticket, self).clean()
    #     quantity = self.cleaned_data.get("quantity")
    #     product = self.cleaned_data.get("product")
    #     amount_product = Product.objects.get(product=product).amount
    #
    #     if quantity > amount_product:
    #         raise ValidationError(f"This quantity is not in stock {amount_product}")
