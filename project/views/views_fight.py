from django.shortcuts import render
from project.models import ArmorItem, Player, Attack


def fight(request):

    return render(request, 'fight/arena.html', {
        'player': Player.objects.all(),
        'armor': ArmorItem.objects.all(),
        'attack': Attack.objects.all(),
    })
