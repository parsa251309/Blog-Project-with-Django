from django import forms
from django.contrib.auth.models import User


class AddBlogForm(forms.Form):
    title = forms.CharField(max_length=100,required=True,label="Title:",widget=forms.TextInput(attrs={"class":"form-control"}))
    content = forms.CharField(required=True,label="Content:",widget=forms.Textarea(attrs={"rows":4,"class":"form-control"}))
    

