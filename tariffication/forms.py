from django import forms
from .models import ServiceGroup


# Форма группировки услуг
class ServiceGroupForm(forms.ModelForm):
    class Meta:
        model = ServiceGroup
        fields = ['title']
