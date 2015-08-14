from django.shortcuts import render
from project.models import Player, ArmorItem, ClassName, Attack


def index(request, p):
    gamer = Player.objects.get(name=p)
    return render(request, 'player/index.html', {'p': gamer})
