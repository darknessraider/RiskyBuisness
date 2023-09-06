from django.shortcuts import render
from player.models import Player
from django.http import JsonResponse
from login.models import Member
import json


def get_balance(request):
    member = Member.objects.filter(username=request.session["username"])[0]
    print(member.player.balance)
    return JsonResponse({'balance': member.player.balance})
