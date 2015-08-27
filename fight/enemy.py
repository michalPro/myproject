from project.models import Player, ClassName, Enemy
from random import randint, random


def easyEnemy(p):
    e = Enemy.objects.get(name='Easy Enemy')
    gamer = Player.objects.get(pk=p)
    suma = gamer.strength + gamer.agility
    min_value = float(suma) * 0.2
    suma = round(float(suma) * 0.6, 0)
    e.level = gamer.level
    ran = randint(1, suma-1)
    e.strength = min_value + ran
    suma -= ran
    e.agility = min_value + suma
    e.maxhealth = randint(round(float(gamer.maxhealth)*0.8, 0), round(float(gamer.maxhealth) * 0.9, 0))
    e.maxmana = 50 + 5 * gamer.level
    e.mana = e.maxmana
    e.armor = e.level * 10
    e.health = e.maxhealth
    e.attack = round(e.strength * 0.9, 0)
    e.dot_damage = 0
    e.dot_rounds = 0
    e.save()


def mediumEnemy(p):
    e = Enemy.objects.get(name='Medium Enemy')
    gamer = Player.objects.get(pk=p)
    suma = gamer.strength + gamer.agility
    min_value = float(suma) * 0.2
    suma = round(float(suma) * 0.6, 0)
    e.level = gamer.level
    ran = randint(1, suma-1)
    e.strength = min_value + ran
    suma -= ran
    e.agility = min_value + suma
    e.maxhealth = randint(round(float(gamer.maxhealth)*0.9, 0), float(gamer.maxhealth))
    e.maxmana = 50 + 5 * gamer.level
    e.mana = e.maxmana
    e.health = e.maxhealth
    e.armor = e.level * 20
    e.attack = round(e.strength * 0.9, 0)
    e.dot_damage = 0
    e.dot_rounds = 0
    e.save()


def hardEnemy(p):
    e = Enemy.objects.get(name='Hard Enemy')
    gamer = Player.objects.get(pk=p)
    suma = gamer.strength + gamer.agility
    min_value = float(suma) * 0.2
    suma = round(float(suma) * 0.6, 0)
    e.level = gamer.level
    ran = randint(1, suma-1)
    e.strength = min_value + ran
    suma -= ran
    e.agility = min_value + suma
    e.maxhealth = randint(float(gamer.maxhealth), round(float(gamer.maxhealth) * 1.1, 0))
    e.maxmana = 50 + 5 * gamer.level
    e.mana = e.maxmana
    e.health = e.maxhealth
    e.armor = e.level * 30
    e.attack = round(e.strength * 0.9, 0)
    e.dot_damage = 0
    e.dot_rounds = 0
    e.save()

