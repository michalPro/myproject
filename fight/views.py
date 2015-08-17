from django.shortcuts import render
from fight.enemy import easyEnemy, hardEnemy, mediumEnemy
from project.models import Player, ArmorItem, Attack, Enemy


def index(request, p):
    easyEnemy(p)
    mediumEnemy(p)
    hardEnemy(p)
    return render(request, 'fight/arena.html', {
        'p': Player.objects.get(pk=p),
        'ee': Enemy.objects.get(name='Easy Enemy'),
        'me': Enemy.objects.get(name='Medium Enemy'),
        'he': Enemy.objects.get(name='Hard Enemy'),
    })


def arenalevel(request, p, e):
    gamer = Player.objects.get(pk=p)
    if e == "Easy Enemy":
        e = Enemy.objects.get(name='Easy Enemy')
    elif e == "Medium Enemy":
        e = Enemy.objects.get(name='Medium Enemy')
    else:
        e = Enemy.objects.get(name='Hard Enemy')

    ph = gamer.health * 100 / gamer.maxhealth
    pm = gamer.mana * 100 / gamer.maxmana
    return render(request, 'fight/arenalevel.html', {
        'p': gamer,
        'e': e,
        'health': ph,
        'mana': pm,
        'armor': ArmorItem.objects.all(),
        'attack': Attack.objects.all(),
    })
