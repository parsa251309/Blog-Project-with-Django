from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="blogs",blank=False,unique=False)
    title = models.CharField(max_length=100,blank=False)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    content = models.CharField(max_length=300,blank=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=False,unique=False)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name="comments")

    def __str__(self):
        return f"{self.content}"