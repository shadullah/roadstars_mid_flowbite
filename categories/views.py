from django.shortcuts import render

# Create your views here.
def categories(req):
    return render(req, 'categories.html')