from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def login_show(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())
