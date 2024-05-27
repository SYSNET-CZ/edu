from django import forms

from .models import Ticket, Order


class TicketModelForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["destination", "price"]


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["first_name", "last_name", "email", "amount"]
