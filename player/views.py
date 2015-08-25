from django.shortcuts import render
from project.models import Player, ArmorItem


def index(request, p):
    gamer = Player.objects.get(pk=p)
    gold_to_pay = int(round(((float(gamer.maxhealth) - float(gamer.health))/10.0
                        + (float(gamer.maxmana) - float(gamer.mana))/5.0) * (float(gamer.level) / 8.0), 0))

    return render(request, 'player/index.html', {
        'p': gamer,
        'armor': ArmorItem.objects.get(name=gamer.armorid).value,
        'pay': int(gold_to_pay),
        'health': gamer.health * 100 / gamer.maxhealth,
        'mana': gamer.mana * 100 / gamer.maxmana,
    })
