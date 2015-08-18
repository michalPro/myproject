from django.shortcuts import render
from project.models import ArmorItem, Player, Attack, Enemy
from django.shortcuts import HttpResponse
from random import random
import math


def player_attack(request):

    player = Player.objects.get(name=request.GET['player'])
    enemy = Enemy.objects.get(name=request.GET['enemy'])

    if request.GET['special'] != "normal":
        special = Attack.objects.get(name=request.GET['special'])

    ph = enemy.health * 100 / enemy.maxhealth
    pm = enemy.mana * 100 / enemy.maxmana

    max_agi = enemy.agility + player.agility
    myrand = random()

    if myrand >= (enemy.agility/max_agi):
        if enemy.health > 0:
            attack_amount = float(player.attack) * (1.0 - ((float(enemy.armor) / float(enemy.level)) / 100.0))
            if enemy.health < attack_amount:
                enemy.health = 0
            else:
                health_left = float(enemy.health) - attack_amount
                enemy.health = int(round(health_left, 0))
    else:
        return render(request, 'fight/partial_view_enemy.html', {
            'e': enemy,
            'health': ph,
            'mana': pm,
        })

    enemy.save()
    return render(request, 'fight/partial_view_enemy.html', {
        'e': enemy,
        'p': player,
        'health': ph,
        'mana': pm,
        'armor': ArmorItem.objects.all(),
        'attack': Attack.objects.all(),
    })


def console(request):
    return render(request, 'fight/partial_view_console_log.html', {
        'enemy': Enemy.objects.get(name=request.GET['enemy']),
        'player': Player.objects.get(name=request.GET['player']),
    })


def enemy_attack(request):
    player = Player.objects.get(name=request.GET['player'])
    enemy = Enemy.objects.get(name=request.GET['enemy'])

    ph = player.health * 100 / player.maxhealth
    pm = player.mana * 100 / player.maxmana

    player.save()

    return render(request, 'fight/partial_view_player.html', {
        'e': enemy,
        'p': player,
        'health': ph,
        'mana': pm,
        'armor': ArmorItem.objects.all(),
    })


def partial_view_player(request):
    return render(request, 'fight/partial_view_player.html',)


def partial_view_enemy(request):
    return render(request, 'fight/partial_view_enemy.html',)


def partial_view_console_log(request):
    return render(request, 'fight/partial_view_console_log.html',)
