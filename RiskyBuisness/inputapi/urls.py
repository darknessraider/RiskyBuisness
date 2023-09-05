from django.urls import path
from . import views

urlpatterns = [
        path('increment_balance', views.increment_balance, name='increment_balance')

]
