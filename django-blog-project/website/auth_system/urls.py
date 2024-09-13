from . import views
from django.urls import path

urlpatterns = [
    path("login/",views.login_user,name="auth_system_login"),
    path("signup/",views.signup_user,name="auth_system_signup"),
    path("logout/",views.logout_user,name="auth_system_logout"),
]
