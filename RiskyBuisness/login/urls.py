from django.urls import path
from . import views

urlpatterns = [
        path('', views.login_show, name = "login"),
        path('signup/', views.signup_show, name = "signup")
]
