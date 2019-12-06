from django import forms
from .models import masege

class masegeForm(forms.ModelForm):

    class Meta:
        model = masege
        fields = ( 'text',)