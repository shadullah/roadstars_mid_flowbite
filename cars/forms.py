from django import forms 
from . models import Cars

class carsForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'