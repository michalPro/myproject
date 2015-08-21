from django.shortcuts import render
from project.models import Player


def index(request, p):
    gamer = Player.objects.get(pk=p)
    return render(request, 'player/index.html', {'p': gamer})
