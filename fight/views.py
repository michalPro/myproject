from django.shortcuts import render
from fight.enemy import EasyEnemy, HardEnemy, MediumEnemy
from project.models import Player, ArmorItem, Attack


def index(request, p):
    return render(request, 'fight/arenalevel.html', {
        'p': Player.objects.get(name=p),
        'ee': EasyEnemy(p),
        'me': MediumEnemy(p),
        'he': HardEnemy(p),
    })


def arena(request, p, e):
    gamer = Player.objects.get(name=p)
    if e == "Easy Enemy":
        e = EasyEnemy(p)
    elif e == "Medium Enemy":
        e = MediumEnemy(p)
    else:
        e = HardEnemy(p)

    ph = gamer.health * 100 / gamer.maxhealth
    pm = gamer.mana * 100 / gamer.maxmana
    return render(request, 'fight/arena.html', {
        'p': gamer,
        'e': e,
        'health': ph,
        'mana': pm,
        'armor': ArmorItem.objects.all(),
        'attack': Attack.objects.all(),
    })
