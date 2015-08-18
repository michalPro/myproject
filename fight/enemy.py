from project.models import Player, ClassName, Enemy
from random import randint, random


def get_class():
    whichclass = random()
    if whichclass < 0.33:
        return ClassName.objects.get(name='Warrior')
    elif 0.33 <= whichclass < 0.66:
        return ClassName.objects.get(name='Thief')
    else:
        return ClassName.objects.get(name='Tankozord')


def get_maxhealth(gamer):
    if random() > 0.5:
            if random() > 0.5:
                return gamer.health + 20
            else:
                return gamer.health + 10
    else:
            if random() > 0.5:
                return gamer.health + 10
            else:
                return gamer.health + 20


def easyEnemy(p):
    e = Enemy.objects.get(name='Easy Enemy')
    e.classname = get_class()
    gamer = Player.objects.get(pk=p)
    suma = gamer.strength + gamer.agility - 30
    e.level = gamer.level
    ran = randint(1, suma-1)
    e.strength = 10 + ran
    suma -= ran
    e.agility = suma + 10
    e.maxhealth = get_maxhealth(gamer)
    e.maxmana = 50
    e.mana = e.maxmana
    e.armor = e.level * 5
    e.health = e.maxhealth
    e.attack = e.strength * 0.9
    e.save()


def mediumEnemy(p):
    e = Enemy.objects.get(name='Medium Enemy')
    e.classname = get_class()
    gamer = Player.objects.get(pk=p)
    suma = gamer.strength + gamer.agility - 20
    e.level = gamer.level
    ran = randint(1, suma-1)
    e.strength = 10 + ran
    suma -= ran
    e.agility = suma + 10
    e.maxhealth = get_maxhealth(gamer)
    e.maxmana = 50
    e.mana = e.maxmana
    e.health = e.maxhealth
    e.armor = e.level * 10
    e.attack = e.strength * 0.9
    e.save()


def hardEnemy(p):
    e = Enemy.objects.get(name='Hard Enemy')
    e.lassname = get_class()
    gamer = Player.objects.get(pk=p)
    suma = gamer.strength + gamer.agility - 10
    e.level = gamer.level
    ran = randint(1, suma-1)
    e.strength = 10 + ran
    suma -= ran
    e.agility = suma + 10
    e.maxhealth = get_maxhealth(gamer)
    e.maxmana = 50
    e.mana = e.maxmana
    e.health = e.maxhealth
    e.armor = e.level * 15
    e.attack = e.strength * 0.9
    e.save()
