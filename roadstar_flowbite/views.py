from django.shortcuts import render
from cars.models import Cars
from categories.models import Brand
def home(request, brand_slug=None):
    data = Cars.objects.all()
    if brand_slug is not None:
        brand = Brand.objects.get(slug = brand_slug)
        data = Cars.objects.filter(brand=brand)
    brand = Brand.objects.all()
    return render(request, 'home.html', {'data': data, 'brand': brand})