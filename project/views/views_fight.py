from django.shortcuts import render
from project.models import ArmorItem, Player, Attack


# def get_enemy(request):


def fight(request):
    return render(request, 'fight/arena.html', {
        'player': Player.objects.all(),
        'armor': ArmorItem.objects.all(),
        'attack': Attack.objects.all(),
    })


def partial_view(request):
    return render(request, 'fight/partial_view.html',)

# def attack_result(request):

# def special_attack_result(request):

