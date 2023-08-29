from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseBadRequest, JsonResponse
import json

def game_show(request):

    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            print(data["payload"])
            return JsonResponse({'status': 'Valid request'})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    
    if 'username' in request.session :
        username = request.session["username"]
    else:
        username = None

    template = loader.get_template('game.html')
    return HttpResponse(template.render({'username': username}))

