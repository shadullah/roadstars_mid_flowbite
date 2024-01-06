from django.shortcuts import render

# Create your views here.
def cars(req):
    return render(req, 'cars.html')