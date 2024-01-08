from django.shortcuts import render,redirect
from . import forms 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile

# Create your views here.
def register(req):
    if req.method == 'POST':
        reg_form = forms.RegForm(req.POST)
        if reg_form.is_valid():
            reg_form.save()
            return redirect('register')
    else:
        reg_form = forms.RegForm()
    return render(req, 'register.html', {'form': reg_form, 'type': 'Register'})

def userLogin(req):
    if req.method == 'POST':
        form = AuthenticationForm(req, req.POST)
        if form.is_valid():
            user_name= form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            user = authenticate(username=user_name, password= userpass)
            if user is not None:
                login(req, user)
                return redirect('home')
            else:
                return redirect('signup')
    else:
        form = AuthenticationForm()
        return render(req, 'register.html', {'form': form, 'type': 'Login'})

@login_required
def profile(req):
    # profile_form = forms.RegForm(instance=req.user)
    try:
        user_profile = UserProfile.objects.get(user=req.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=req.user)

    return render(req, 'profile.html', {'user_profile': user_profile})

def editProfile(req):
    if req.method == 'POST':
        edit_form = forms.changeUserinfo(req.POST, instance=req.user)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('profile')
    else:
        edit_form = forms.RegForm(instance=req.user)
    return render(req, 'edit_profile.html', {'form' : edit_form})


def user_logout(req):
    logout(req)
    return redirect('login')