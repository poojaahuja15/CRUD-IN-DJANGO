from .models import vehicle
from django import forms
from django.core import validators

class vehicleForm(forms.ModelForm):
    class Meta:
        model = vehicle
        fields = "__all__"
        widgets = {
            'vehicletype' : forms.TextInput(attrs={'class':'form-control'}),
            'modelname': forms.TextInput(attrs={'class': 'form-control'}),
            'vehiclecolor': forms.TextInput(attrs={'class': 'form-control'}),
            'enginetype': forms.TextInput(attrs={'class': 'form-control'}),
        }
