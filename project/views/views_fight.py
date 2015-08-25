from django.shortcuts import render
from project.models import ArmorItem, Player, Attack, Enemy, AttackLog
from project.service.service_attack import p_attack, e_attack, receive_exp
from django.shortcuts import redirect


def player_attack(request):

    player = Player.objects.get(name=request.GET['player'])
    enemy = Enemy.objects.get(name=request.GET['enemy'])
    special = Attack.objects.get(name=request.GET['special'])
    attack_log = AttackLog(playerdamage=0, enemydamage=0)

    is_double = 1.0
    if special.name == 'Double Attack':
        is_double = 2.0
    enemy, player = p_attack(enemy, player, special, attack_log, is_double)

    enemy.save()
    player.save()

    if enemy.health <= 0:
        received_exp = receive_exp(enemy, player)
        enemy.dot_rounds = 0
        enemy.dot_damage = 0
        if received_exp+player.experience > player.requiredexp:
            player.level += 1
            exp_left = player.requiredexp - player.experience
            player.requiredexp = 400 * player.level
            player.experience = exp_left
            player.strength += 6
            player.agility += 5
            player.maxhealth += 50
            player.maxmana += 7
            player.attack = 0.9 * player.strength
        else:
            player.experience += received_exp
        player.gold += received_exp/2 * player.level

        player.save()

        return render(request, 'fight/victory.html', {
            'p': player,
            'defeated': enemy,
        })
    else:
        return render(request, 'fight/partial_view_enemy.html', {
            'e': enemy,
            'p': player,
            'health': enemy.health * 100 / enemy.maxhealth,
            'mana': enemy.mana * 100 / enemy.maxmana,
        })


def console_log(request):

    return render(request, 'fight/partial_view_console_log.html', {
        'enemy': Enemy.objects.get(name=request.GET['enemy']),
        'player': Player.objects.get(name=request.GET['player']),
        'log': AttackLog.objects.all(),
    })


def enemy_attack(request):

    player = Player.objects.get(name=request.GET['player'])
    enemy = Enemy.objects.get(name=request.GET['enemy'])
    special = Attack.objects.all()
    attack_log = AttackLog.objects.all()
    attack_log = attack_log.get(pk=len(attack_log))
    armor = ArmorItem.objects.get(name=player.armorid).value

    enemy, player = e_attack(player, enemy, special, attack_log, armor)

    enemy.save()
    player.save()

    if player.health <= 0:
        player.dot_rounds = 0
        player.dot_damage = 0
        player.health = player.maxhealth
        player.mana = player.maxmana
        player.experience -= player.requiredexp * 0.05
        player.save()

        return render(request, 'fight/victory.html', {
            'p': player,
            'defeated': player,
        })
    return render(request, 'fight/partial_view_player.html', {
        'e': enemy,
        'p': player,
        'health': player.health * 100 / player.maxhealth,
        'mana': player.mana * 100 / player.maxmana,
        'armor': ArmorItem.objects.get(name=player.armorid).value,
        'attack': Attack.objects.all(),
    })


def victory(request):
    return render(request, 'fight/victory.html',)


def partial_view_player(request):
    return render(request, 'fight/partial_view_player.html',)


def partial_view_enemy(request):
    return render(request, 'fight/partial_view_enemy.html',)


def partial_view_console_log(request):
    return render(request, 'fight/partial_view_console_log.html',)
