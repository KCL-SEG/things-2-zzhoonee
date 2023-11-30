"""Forms of the project."""

from django import forms
from things.models import Thing

class ThingForm(forms.Form):

    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {'description': forms.Textarea(), 'quantity': forms.NumberInput()}

