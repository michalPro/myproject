from django.shortcuts import render
from project.models import Player, ArmorItem, Elixir


def index(request, p):
    gamer = Player.objects.get(pk=p)
    for elixir in Elixir.objects.all():
        elixir.price = (gamer.requiredexp / gamer.level) * elixir.multiplier
        elixir.save()
    gold_to_pay = int(round(((float(gamer.maxhealth) - float(gamer.health))/15.0
                        + (float(gamer.maxmana) - float(gamer.mana))/7.0) * (float(gamer.level)), 0))

    return render(request, 'player/index.html', {
        'p': gamer,
        'armor': ArmorItem.objects.get(name=gamer.armorid).value,
        'pay': int(gold_to_pay),
        'health': gamer.health * 100 / gamer.maxhealth,
        'mana': gamer.mana * 100 / gamer.maxmana,
    })
