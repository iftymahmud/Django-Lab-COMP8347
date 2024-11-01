from django import forms
from .models import OrderVehicle


class OrderVehicleForm(forms.ModelForm):
    class Meta:
        model = OrderVehicle
        fields = ['vehicle', 'buyer', 'quantity']
        labels = {
            'quantity': 'Number of Vehicles Ordered',
        }
        widgets = {
            'buyer': forms.Select(),
        }


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)
