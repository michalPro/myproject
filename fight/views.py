from django.shortcuts import render
from fight.enemy import easyEnemy, hardEnemy, mediumEnemy
from project.models import Player, ArmorItem, Attack, Enemy, AttackLog, Elixir


def index(request, p):
    easyEnemy(p)
    mediumEnemy(p)
    hardEnemy(p)
    return render(request, 'fight/arena.html', {
        'p': Player.objects.get(pk=p),
        'ee': Enemy.objects.get(name='Easy Enemy'),
        'me': Enemy.objects.get(name='Medium Enemy'),
        'he': Enemy.objects.get(name='Hard Enemy'),
        'eb': Enemy.objects.get(name='Easy Boss'),
        'mb': Enemy.objects.get(name='Medium Boss'),
        'hb': Enemy.objects.get(name='Hard Boss'),
    })


def arenalevel(request, p, e):
    gamer = Player.objects.get(pk=p)
    if e == "Easy Enemy":
        e = Enemy.objects.get(name=e.name)
    elif e == "Medium Enemy":
        e = Enemy.objects.get(name='Medium Enemy')
    elif e == "Hard Enemy":
        e = Enemy.objects.get(name='Hard Enemy')
    elif e == "Easy Boss":
        e = Enemy.objects.get(name='Easy Boss')
    elif e == "Medium Boss":
        e = Enemy.objects.get(name='Medium Boss')
    else:
        e = Enemy.objects.get(name='Hard Boss')
    AttackLog.objects.all().delete()

    return render(request, 'fight/arenalevel.html', {
        'p': gamer,
        'e': e,
        'health': gamer.health * 100 / gamer.maxhealth,
        'mana': gamer.mana * 100 / gamer.maxmana,
        'armor': ArmorItem.objects.get(name=gamer.armorid).value,
        'attack': Attack.objects.all(),
        'log': AttackLog.objects.all(),
        'elixir': Elixir.objects.all(),
    })
