from django.shortcuts import render
from project.models import ArmorItem, Player, Attack, Enemy
from django.shortcuts import HttpResponse
from random import random
import math


def attack(enemy, player, max_agi, special):
    myrand = random()

    if special.requiredmana < player.mana and player.level >=special.requiredlv:
        if myrand >= (enemy.agility/max_agi):
            if enemy.health > 0:
                attack_amount = (float(player.attack) * special.bonusattack) * (1.0 - ((float(enemy.armor) / float(enemy.level)) / 100.0))
                if enemy.health < attack_amount:
                    enemy.health = 0
                else:
                    health_left = float(enemy.health) - attack_amount
                    enemy.health = int(round(health_left, 0))
                    player.mana -= special.requiredmana
                return enemy, player
        else:
            return enemy, player
    else:
        #no mana or lv
        return


def player_attack(request):

    player = Player.objects.get(name=request.GET['player'])
    enemy = Enemy.objects.get(name=request.GET['enemy'])

    max_agi = enemy.agility + player.agility

    special = Attack.objects.get(name=request.GET['special'])
    enemy, player = attack(enemy, player, max_agi, special)
    enemy.save()
    player.save()
    #return


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
