from django import forms
from .models import shirt




class shirtform(forms.ModelForm):
    class Meta:#sub class
        model=shirt
        fields=['brand','size','price','rating']