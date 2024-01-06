from django.shortcuts import render

# Create your views here.
def users(req):
    return render(req, 'users.html')