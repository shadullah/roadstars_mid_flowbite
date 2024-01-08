from django.shortcuts import render
from cars.models import Cars
from categories.models import Brand
def home(request):
    data = Cars.objects.all()
    brand = Brand.objects.all()
    return render(request, 'home.html', {'data': data, 'brand': brand})