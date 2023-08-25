from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def game_show(request):
    
    if 'username' in request.session :
        username = request.session["username"]
    else:
        username = None

    template = loader.get_template('game.html')
    return HttpResponse(template.render({'username': username}))

