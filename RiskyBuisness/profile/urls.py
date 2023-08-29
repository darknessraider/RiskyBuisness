from django.urls import path
from . import views
urlpatterns = [
	path('', views.home_show, name = 'profile'),
] 
