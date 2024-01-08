from typing import Any
from django.shortcuts import render, get_object_or_404,redirect
from .models import Cars
from . import models
from django.views.generic import DetailView
from users.models import UserProfile
from . import forms

# Create your views here.
def cars(req):
    data = Cars.objects.all()
    return render(req, 'cars.html',{'data':data})


class DetailsCAr(DetailView):
    model = models.Cars
    pk_url_kwarg = 'id'
    template_name = 'cars.html'

    def post(self, req, *args, **kwargs):
        cmmnt_form = forms.CmntForm(data=self.request.POST)
        car = self.get_object()
        if cmmnt_form.is_valid():
            new_com = cmmnt_form.save(commit=False)
            new_com.cars = car
            print(new_com)
            new_com.save()
        return self.get(req, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        cmmnt_form = forms.CmntForm()

        context['comments'] = comments
        context['comment_form']= cmmnt_form
        return context
    

def buy_now(req, car_id):
    car = get_object_or_404(Cars, pk=car_id)
    
    if car.quantity>0:
        car.quantity-=1
        car.save()

        user_profile = UserProfile.objects.get(user=req.user)
        user_profile.borrowed_cars.add(car)
        user_profile.save()
    
    return redirect('details', id=car_id)