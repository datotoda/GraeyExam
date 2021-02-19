from django import forms
from django.forms import ModelChoiceField

from ecommerce.models import Ticket, Order


class OrderForm(forms.ModelForm):
    ticket = ModelChoiceField(queryset=Ticket.objects.all())

    class Meta:
        model = Order
        fields = ('ticket')
