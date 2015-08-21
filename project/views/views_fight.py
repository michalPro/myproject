from django.shortcuts import render
from project.models import ArmorItem, Player, Attack, Enemy, AttackLog
from project.service.service_attack import p_attack, e_attack, receive_exp
from django.shortcuts import redirect


def player_attack(request):

    player = Player.objects.get(name=request.GET['player'])
    enemy = Enemy.objects.get(name=request.GET['enemy'])
    special = Attack.objects.get(name=request.GET['special'])
    attack_log = AttackLog(playerdamage=0, enemydamage=0)

    enemy, player = p_attack(enemy, player, special, attack_log)

    enemy.save()
    player.save()

    if enemy.health <= 0:
        received_exp = receive_exp(enemy, player)
        if received_exp+player.experience > player.requiredexp:
            player.level += 1
            exp_left = player.requiredexp - player.experience
            player.requiredexp = 400 * player.level
            player.experience = exp_left
        else:
            player.experience += received_exp

        player.health = player.maxhealth
        player.mana = player.maxmana
        player.save()

        #return redirect('fight/victory.html')
        return render(request, 'fight/victory.html', {
            'p': player,
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

    enemy, player = e_attack(player, enemy, special, attack_log)

    enemy.save()
    player.save()

    return render(request, 'fight/partial_view_player.html', {
        'e': enemy,
        'p': player,
        'health': player.health * 100 / player.maxhealth,
        'mana': player.mana * 100 / player.maxmana,
    })


def victory(request):
    return render(request, 'fight/victory.html',)


def partial_view_player(request):
    return render(request, 'fight/partial_view_player.html',)


def partial_view_enemy(request):
    return render(request, 'fight/partial_view_enemy.html',)


def partial_view_console_log(request):
    return render(request, 'fight/partial_view_console_log.html',)
