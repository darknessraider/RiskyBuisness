from django.shortcuts import render
from player.models import Player
from django.http import JsonResponse
from login.models import Member

def check_valid(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest' 
    if is_ajax:
        if request.method == 'POST':
            return True
    else:
        return False


def increment_balance(request):
    if check_valid(request):
        member = Member.objects.filter(username=request.session["username"])[0]
        try:
            member.player.increment_balance()
        except:
            player = Player.objects.create(balance=1, member=member)
            player.save()
        print(member.player.balance)
        return JsonResponse({'balance': member.player.balance})
    else:
        return JsonResponse({'status': 'Invalid request'})

