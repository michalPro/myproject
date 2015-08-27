from django.shortcuts import render
from project.models import ArmorItem, Player, Attack, Enemy, AttackLog, Elixir
from project.service.service_attack import p_attack, e_attack, receive_exp


def player_attack(request):

    player = Player.objects.get(name=request.GET['player'])
    enemy = Enemy.objects.get(name=request.GET['enemy'])
    special = Attack.objects.get(name=request.GET['special'])
    attack_log = AttackLog(playerdamage=0, enemydamage=0, player_bonus_attack=0, enemy_bonus_attack=0)

    is_double = 1.0
    if special.name == 'Double Attack':
        is_double = 2.0
    enemy, player = p_attack(enemy, player, special, attack_log, is_double)

    enemy.save()
    player.save()

    if enemy.health <= 0:
        received_exp = receive_exp(enemy, player)
        received_gold = int(round(float(received_exp) / player.level, 0))
        player.gold += received_gold
        reset_dot(player, enemy)
        if received_exp + player.experience > player.requiredexp:
            player.level += 1
            exp_left = player.requiredexp - player.experience
            player.requiredexp *= 2
            player.experience = exp_left
            player.strength += 6
            player.agility += 5
            player.maxhealth += 90
            player.maxmana += 7
            player.health = player.maxhealth
            player.mana = player.maxmana
            player.attack = 0.9 * player.strength
        else:
            player.experience += received_exp

        player.save()

        return render(request, 'fight/victory.html', {
            'p': player,
            'defeated': enemy,
            'gold': received_gold,
            'exp': received_exp,
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
        reset_dot(player, enemy)
        player.health = player.maxhealth
        player.mana = player.maxmana
        received_exp = player.requiredexp * 0.05
        player.experience -= received_exp
        if player.experience < 0:
            player.experience = 0
        player.save()
        received_gold = 0

        return render(request, 'fight/victory.html', {
            'p': player,
            'defeated': player,
            'gold': received_gold,
            'exp': -received_exp,
        })
    return render(request, 'fight/partial_view_player.html', {
        'e': enemy,
        'p': player,
        'health': player.health * 100 / player.maxhealth,
        'mana': player.mana * 100 / player.maxmana,
        'armor': ArmorItem.objects.get(name=player.armorid).value,
        'attack': Attack.objects.all(),
    })


def use_elixir(request):
    player = Player.objects.get(name=request.GET['player'])
    enemy = Enemy.objects.get(name=request.GET['enemy'])
    elixir = Elixir.objects.get(name=request.GET['elixir'])

    if 'Small' in elixir.name:
        player.small_elixir -= 1
    elif 'Medium' in elixir.name:
        player.medium_elixir -= 1
    elif 'Big' in elixir.name:
        player.big_elixir -= 1
    else:
        player.ultimate_elixir -= 1

    player.health += player.maxhealth * elixir.health_restore / 100
    player.mana += player.maxmana * elixir.mana_restore / 100
    player.save()
    return render(request, 'fight/partial_view_enemy.html', {
        'e': enemy,
        'p': player,
        'health': enemy.health * 100 / enemy.maxhealth,
        'mana': enemy.mana * 100 / enemy.maxmana,
    })


def victory(request):
    return render(request, 'fight/victory.html',)


def partial_view_player(request):
    return render(request, 'fight/partial_view_player.html',)


def partial_view_enemy(request):
    return render(request, 'fight/partial_view_enemy.html',)


def partial_view_console_log(request):
    return render(request, 'fight/partial_view_console_log.html',)


def reset_dot(player, enemy):
    player.dot_rounds = 0
    player.dot_damage = 0
    enemy.dot_damage = 0
    enemy.dot_rounds = 0
