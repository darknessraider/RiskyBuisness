from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home_show(request):
    return HttpResponse(request.session["username"])
