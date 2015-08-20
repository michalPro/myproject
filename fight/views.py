from django.shortcuts import render
from fight.enemy import easyEnemy, hardEnemy, mediumEnemy
from project.models import Player, ArmorItem, Attack, Enemy, AttackLog


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

    attack_log = AttackLog.objects.all()
    attack_log.delete()

    return render(request, 'fight/arenalevel.html', {
        'p': gamer,
        'e': e,
        'health': gamer.health * 100 / gamer.maxhealth,
        'mana': gamer.mana * 100 / gamer.maxmana,
        'armor': ArmorItem.objects.all(),
        'attack': Attack.objects.all(),
    })
