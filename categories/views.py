from django.shortcuts import render, redirect
from . import forms 

# Create your views here.
def categories(req):
    brand_form = forms.brandForm()
    return render(req, 'categories.html', {'form': brand_form})

    # if req.method == 'POST':
    #     brand_form = forms.brandForm(req.POST)
    #     if brand_form.is_valid():
    #         brand_form.save()
    #         return redirect('home')
    # else:
    #     brand_form = forms.brandForm()
    # return render(req, 'categories.html', {'form': brand_form})