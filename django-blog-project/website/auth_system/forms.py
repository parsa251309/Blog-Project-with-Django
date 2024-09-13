from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(forms.Form):
    first_name = forms.CharField(label="First Name:",max_length=100,required=True,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name:",max_length=100,required=True,widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username:",max_length=100,required=True,widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(label="Email:",max_length=100,required=True,widget=forms.EmailInput(attrs={"class":"form-control"}))
    password1 = forms.CharField(label="Password:",max_length=100,required=True,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(label="Confrim Password:",max_length=100,required=True,widget=forms.PasswordInput(attrs={"class":"form-control"}))



class LoginForm(forms.Form):
    username = forms.CharField(label="Username:",max_length=100,required=True,widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password:",max_length=100,required=True,widget=forms.PasswordInput(attrs={"class":"form-control"}))