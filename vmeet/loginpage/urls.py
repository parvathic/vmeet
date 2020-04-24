from django.conf.urls import url
from loginpage import views
from django.contrib.auth import views as auth_views

from django.urls import path

urlpatterns = [
    url(r'^$', views.loginpage),
    url(r'^login/$', auth_views.LoginView.as_view(template_name="loginpage/login.html"), name="login"),
    
]
