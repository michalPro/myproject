from django.shortcuts import render
from project.models import Player, ArmorItem


def index(request, p):
    gamer = Player.objects.get(pk=p)
    return render(request, 'player/index.html', {
        'p': gamer,
        'armor': ArmorItem.objects.get(name=gamer.armorid).value,
    })
