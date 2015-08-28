from random import random, randint
from project.models import AttackLog, Elixir


def is_attack():
    if random() > 0.04:
        return True
    return False


def get_dodge(attacker, enemy):

    chance = float(float((enemy.agility * 50) / (attacker.agility + enemy.agility)) / 100)
    if random() > chance:
        return False
    return True


def my_range(start, end, step):
    while start >= end:
        yield start
        start -= step


def get_boss_multiplier(blvl, p, m):
    s = int(m * 10)
    for x in range(1, s-10):
        if p == x + blvl:
            m -= x * 0.2
    if m < 1.0:
        m = 1.0
    return m


def receive_exp(enemy, player):
    if enemy.name == 'Easy Enemy':
        multiplier = 1.0
    elif enemy.name == 'Medium Enemy':
        multiplier = 1.5
    elif enemy.name == 'Hard Enemy':
        multiplier = 2.0
    elif enemy.name == 'Easy Boss':
        multiplier = get_boss_multiplier(enemy.level, player.level, 3.0)
    elif enemy.name == 'Medium Boss':
        multiplier = get_boss_multiplier(enemy.level, player.level, 4.0)
    else:
        multiplier = get_boss_multiplier(enemy.level, player.level, 5.0)
    level_bonus = 1.0
    if player.level < 10:
        y = 1
        for x in my_range(5.5, 1, 0.5):
            if y == player.level:
                level_bonus = x
            y += 1
    if player.health == player.maxhealth:
        player.health -= 1

    return round(float(multiplier) * ((float(player.maxhealth)-float(player.health))/float(player.maxhealth))
                 * player.requiredexp * 0.1 * level_bonus, 0)


def p_attack(enemy, player, special, attack_log, is_double):

    bonus = randint(0, int(player.attack * 0.1))
    dodge = get_dodge(player, enemy)
    if not dodge:
        if enemy.health > 0:
            attack_amount = ((float(player.attack) * (float(special.bonusattack))) *
                             (1.0 - ((float(enemy.armor) / float(enemy.level)) / 100.0)) + float(bonus)) * is_double

            if enemy.health < attack_amount:
                enemy.health = 0
            else:
                if special.name == 'Bleed':
                    enemy.dot_damage = int(round(attack_amount, 0))
                    enemy.dot_rounds += 2
                    enemy.health -= enemy.dot_damage
                else:
                    if enemy.dot_rounds > 0:
                        attack_log.player_bonus_attack = enemy.dot_damage
                        enemy.dot_rounds -= 1
                    health_left = float(enemy.health) - attack_amount
                    enemy.health = int(round(health_left, 0))
                player.mana -= special.requiredmana

            attack_log.playerdamage = int(round(attack_amount, 0))
            attack_log.player_attack_name = special.name
    else:
        attack_amount = 0
        if enemy.dot_rounds > 0:
            attack_amount += enemy.dot_damage
            enemy.dot_rounds -= 1
            attack_log.player_attack_name = "Bleed"
            enemy.health -= attack_amount
        attack_log.playerdamage = attack_amount

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
    bonus = randint(0, int(enemy.attack * 0.1))
    if is_attack():
        if not dodge:
            if player.health > 0:
                attack_amount = (float(enemy.attack) * (float(attack.bonusattack))) *\
                                (1.0 - ((float(armor) / float(player.level)) / 100.0)) + float(bonus)

                if player.health < attack_amount:
                    player.health = 0
                else:
                    if attack.name == 'Bleed':
                        player.dot_damage = int(round(attack_amount, 0))
                        player.dot_rounds += 2
                        player.health -= player.dot_damage
                    else:
                        if player.dot_rounds > 0:
                            attack_log.enemy_bonus_attack = player.dot_damage
                            player.dot_rounds -= 1
                        health_left = float(player.health) - attack_amount
                        player.health = int(round(health_left, 0))
                    enemy.mana -= attack.requiredmana

                attack_log.enemydamage = int(round(attack_amount, 0))
                attack_log.enemy_attack_name = attack.name
        else:
            attack_amount = 0
            if player.dot_rounds > 0:
                attack_amount += player.dot_damage
                player.dot_rounds -= 1
                attack_log.enemy_attack_name = "Bleed"
                player.health -= attack_amount
            attack_log.enemydamage = attack_amount
    else:
        chance = random()
        if chance < 0.5:
            e = Elixir.objects.get(name='Small Elixir')
            enemy.health += enemy.maxhealth * e.health_restore
        elif 0.5 <= chance < 0.75:
            e = Elixir.objects.get(name='Medium Elixir')
            enemy.health += enemy.maxhealth * e.health_restore
        elif 0.75 <= chance < 0.95:
            e = Elixir.objects.get(name='Big Elixir')
            enemy.health += enemy.maxhealth * e.health_restore
        else:
            e = Elixir.objects.get(name='Ultimate Elixir')
            enemy.health += enemy.maxhealth * e.health_restore
        if enemy.health > enemy.maxhealth:
            enemy.health = enemy.maxhealth

    attack_log.save()
    return enemy, player
