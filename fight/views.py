from django.shortcuts import render
from fight.enemy import easyEnemy, hardEnemy, mediumEnemy
from project.models import Player, ArmorItem, Attack, Enemy, AttackLog, Elixir


def index(request, p):
    easyEnemy(p)
    mediumEnemy(p)
    hardEnemy(p)
    e = Enemy.objects.get(name='Easy Boss')
    e.health = e.maxhealth
    e.mana = e.maxmana
    e.save()
    e = Enemy.objects.get(name='Medium Boss')
    e.health = e.maxhealth
    e.mana = e.maxmana
    e.save()
    e = Enemy.objects.get(name='Hard Boss')
    e.health = e.maxhealth
    e.mana = e.maxmana
    e.save()
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
    e = Enemy.objects.get(name=e)

    AttackLog.objects.all().delete()

    return render(request, 'fight/arenalevel.html', {
        'p': gamer,
        'e': e,
        'armor': ArmorItem.objects.get(name=gamer.armorid).value,
        'attack': Attack.objects.all(),
        'log': AttackLog.objects.all(),
        'elixir': Elixir.objects.all(),
    })
