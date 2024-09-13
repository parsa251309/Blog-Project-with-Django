from django.shortcuts import render,redirect
from . import models
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from . import (models,forms)

from django.contrib.auth.models import User

@login_required
def index(request:HttpRequest):
    
    if (request.method == "POST"):
        selected_id = request.POST.get("btn-submit")
        if (selected_id != None):
            blog_id = int(selected_id)
            comment_text = request.POST.get(f"input-{blog_id}")
            models.Blog.objects.get(id=blog_id).comments.create(content=comment_text,user=request.user)
        return redirect("main_index")

    return render(request,"main/index.html",{"blogs":models.Blog.objects.all()})


@login_required
def add_blog(request:HttpRequest):
    if (request.method == "POST"):
        form = forms.AddBlogForm(request.POST)

        if (form.is_valid()):
            request.user.blogs.create(title=form.cleaned_data["title"],content=form.cleaned_data["content"])
            return redirect("main_index")

    form = forms.AddBlogForm()

    return render(request,"main/add-blog.html",{"form":form})

@login_required
def delete_blog(request:HttpRequest,pk):
    selected_blog = models.Blog.objects.filter(id=pk).first()
    if (selected_blog != None):
        if (selected_blog.user == request.user):
            selected_blog.delete()

    return redirect("main_index")

@login_required
def update_blog(request:HttpRequest,pk):
    selected_blog = models.Blog.objects.filter(id=pk).first()
    if (selected_blog == None):
        return redirect("main_index")
    
    if (selected_blog.user != request.user):
        return redirect("main_index")

    if (request.method == "POST"):
        form = forms.AddBlogForm(request.POST)
        if (form.is_valid()):
            selected_blog.title = form.cleaned_data["title"]
            selected_blog.content = form.cleaned_data["content"]
            selected_blog.save()
            return redirect("main_index")
        

    form = forms.AddBlogForm()
    form.initial["title"] = selected_blog.title
    form.initial["content"] = selected_blog.content

    return render(request,"main/add-blog.html",{"form":form})

@login_required
def get_user_blogs(request:HttpRequest,pk):
    user = User.objects.filter(id=pk).first()
    if (user == None):
        return redirect("main_index")
    
    print(user.blogs.all())

    return render(request,"main/user-blogs.html",{"blogs":user.blogs.all()})