from django import forms 
from . models import Cars,Comment

class carsForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'


class CmntForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ['name', 'body']