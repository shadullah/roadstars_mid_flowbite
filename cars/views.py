from django.shortcuts import render, get_object_or_404,redirect
from .models import Cars
from . import models
from django.views.generic import DetailView
from users.models import UserProfile

# Create your views here.
def cars(req):
    data = Cars.objects.all()
    return render(req, 'cars.html',{'data':data})


class DetailsCAr(DetailView):
    model = models.Cars
    pk_url_kwarg = 'id'
    template_name = 'cars.html'

def buy_now(req, car_id):
    car = get_object_or_404(Cars, pk=car_id)
    
    if car.quantity>0:
        car.quantity-=1
        car.save()

        user_profile = UserProfile.objects.get(user=req.user)
        user_profile.borrowed_cars.add(car)
        user_profile.save()
    
    return redirect('details', id=car_id)