from django.shortcuts import render
from django.http import HttpResponse

def home_show(request):
    return HttpResponse("Hello, World!")
