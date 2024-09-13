from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="main_index"),
    path("add-blog",views.add_blog,name="main_addblog"),
    path("delete/<int:pk>",views.delete_blog,name="main_deleteblog"),
    path("update/<int:pk>",views.update_blog,name="main_updateblog"),
    path("get_user_blogs/<int:pk>",views.get_user_blogs,name="main_get_blogs"),
]
