from django.shortcuts import render
from project.models import ArmorItem, Player, Attack
from django.shortcuts import HttpResponse


# def get_enemy(request):


def fight(request):
    player = request.GET['player']
    enemy = request.GET['enemy']

    return HttpResponse(request.GET['enemy'])


def partial_view(request):
    return render(request, 'fight/partial_view.html',)

# def attack_result(request):

# def special_attack_result(request):

