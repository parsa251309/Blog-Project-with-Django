from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpRequest


# Create your views here.
def login_user(request:HttpRequest):
    
    if (request.method == "POST"):
        form = forms.LoginForm(request.POST)
        if (form.is_valid()):
            user = authenticate(username = form.cleaned_data["username"],password=form.cleaned_data["password"])
            if (user != None):
                login(request,user)
                return redirect("main_index")
                

    form = forms.LoginForm()
    return render(request,"auth/login.html",{"form":form})

def signup_user(response):
    if (response.method == "POST"):
        form = forms.SignUpForm(response.POST)
        if (form.is_valid()):
            if (form.cleaned_data["password1"] == form.cleaned_data["password2"]) and (User.objects.filter(username=form.cleaned_data["username"]).first() == None) and (User.objects.filter(email=form.cleaned_data["email"]).first() == None):
                new_user = User(email=form.cleaned_data["email"],username=form.cleaned_data["username"],password=form.cleaned_data["password1"])            
                new_user.first_name = form.cleaned_data["first_name"]
                new_user.last_name = form.cleaned_data["last_name"]
                new_user.save()
                login(response,new_user)
                return redirect("main_index")


    form = forms.SignUpForm()
    return render(response,"auth/signup.html",{"form":form})

def logout_user(request:HttpRequest):
    if (request.user.is_authenticated):
        logout(request)
        return redirect("main_index")