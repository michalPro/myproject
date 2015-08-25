from random import random, randint
from project.models import AttackLog


def get_dodge(attacker, enemy):

    chance = float(float((enemy.agility * 70) / (attacker.agility + enemy.agility)) / 100)
    if random() > chance:
        return False
    else:
        return True


def receive_exp(enemy, player):
    attack_no = AttackLog.objects.count()
    if enemy.name == 'Easy Enemy':
        multiplier = 1.0
    elif enemy.name == 'Medium Enemy':
        multiplier = 2.0
    else:
        multiplier = 3.0
    return round(float(multiplier) * (float(player.maxhealth)/float(player.health)) * float(attack_no), 0)


def p_attack(enemy, player, special, attack_log, is_double):

    bonus = randint(0, 5)
    dodge = get_dodge(player, enemy)
    if not dodge:
        if enemy.health > 0:
            attack_amount = ((float(player.attack) * (float(special.bonusattack))) *
                             (1.0 - ((float(enemy.armor) / float(enemy.level)) / 100.0)) + float(bonus)) * is_double
            attack_log.playerdamage = int(round(attack_amount, 0))

            if enemy.health < attack_amount:
                enemy.health = 0
            else:
                health_left = float(enemy.health) - attack_amount
                enemy.health = int(round(health_left, 0))
                player.mana -= special.requiredmana
    else:
        attack_log.playerdamage = 0
    attack_log.save()
    return enemy, player


def get_attack(special, enemy, not_get=True):

    attack = special.get(pk=1)
    while not_get:
        special_random = randint(0, 150)

        if special_random <= 50:
            attack = special.get(pk=1)
        elif 50 < special_random <= 75:
            attack = special.get(pk=2)
        elif 75 < special_random <= 100:
            attack = special.get(pk=3)
        elif 100 < special_random <= 125:
            attack = special.get(pk=4)
        else:
            attack = special.get(pk=5)

        if attack.requiredmana <= enemy.mana and enemy.level >= attack.requiredlv:
            not_get = False
    return attack


def e_attack(player, enemy, special, attack_log, armor):

    dodge = get_dodge(enemy, player)
    attack = get_attack(special, enemy)
    bonus = randint(0, 5)

    if not dodge:
        if player.health > 0:
            attack_amount = (float(enemy.attack) * (float(attack.bonusattack))) *\
                            (1.0 - ((float(armor) / float(player.level)) / 100.0)) + float(bonus)
            attack_log.enemydamage = int(round(attack_amount, 0))

            if player.health < attack_amount:
                player.health = 0
            else:
                health_left = float(player.health) - attack_amount
                player.health = int(round(health_left, 0))
                enemy.mana -= attack.requiredmana
    else:
         attack_log.enemydamage = 0

    attack_log.save()
    return enemy, player
