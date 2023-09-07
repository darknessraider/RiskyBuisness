from django.urls import path
from . import views

urlpatterns = [
        path('get_balance', views.get_balance, name='get_balance')

]
