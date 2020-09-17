from django import forms

from .models import Application


class Applyform(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['firstname', 'lastname', 'age', 'phone', 'email', 'gender', 'date', 'cv']