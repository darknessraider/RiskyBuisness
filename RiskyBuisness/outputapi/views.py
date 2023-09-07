from django.shortcuts import render
from player.models import Player
from django.http import JsonResponse
from login.models import Member
import json


def get_balance(request):
    member = Member.objects.filter(username=request.session["username"])[0]

    try:
        return JsonResponse({'balance': member.player.balance})
    except:
        player = Player.objects.create(balance=0, member=member)
        player.save()
        return JsonResponse({'balance': member.player.balance})