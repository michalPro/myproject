from random import random, randint


def p_attack(enemy, player, max_agi, special, attack_log):

    my_random = random()

    if special.requiredmana < player.mana and player.level >= special.requiredlv:
        if my_random >= (enemy.agility/max_agi):
            if enemy.health > 0:
                attack_amount = (float(player.attack) * (float(special.bonusattack))) * \
                    (1.0 - ((float(enemy.armor) / float(enemy.level)) / 100.0))
                attack_log.playerdamage = int(round(attack_amount, 0))

                if enemy.health < attack_amount:
                    enemy.health = 0
                else:
                    health_left = float(enemy.health) - attack_amount
                    enemy.health = int(round(health_left, 0))
                    player.mana -= special.requiredmana
        else:
            attack_log.playerdamage = 0
    enemy.strength = attack_log.playerdamage
    attack_log.save()
    return enemy, player


def get_attack(special, enemy, not_get=True):

    attack = special.get(pk=1)
    while not_get:
        special_random = randint(0, 150)

        if special_random <= 50:
            attack = special.get(pk=1)
        elif 50 > special_random < 75:
            attack = special.get(pk=2)
        elif 75 > special_random < 100:
            attack = special.get(pk=3)
        elif 100 > special_random < 125:
            attack = special.get(pk=4)
        else:
            attack = special.get(pk=5)

        if attack.requiredmana < enemy.mana:
            not_get = False
    return attack


def e_attack(player, enemy, special, max_agi):

    my_random = random()
    attack = get_attack(special, enemy)

    if my_random >= (player.agility/max_agi):
        if player.health > 0:
            attack_amount = (float(enemy.attack) * (float(attack.bonusattack)))

            if player.health < attack_amount:
                player.health = 0
            else:
                health_left = float(player.health) - attack_amount
                player.health = int(round(health_left, 0))
                enemy.mana -= attack.requiredmana

    return enemy, player
