from project.models import Player
from random import randint, random


def get_class():
    whichclass = random()
    if whichclass < 0.33:
        return "Warrior"
    elif 0.33 <= whichclass < 0.66:
        return "Thief"
    else:
        return "Tankozord"


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

class EasyEnemy:
    def __init__(self, p):
        self.classname = get_class()
        self.name = "Easy Enemy"
        gamer = Player.objects.get(name=p)
        suma = gamer.strength + gamer.agility - 30
        self.level = gamer.level
        ran = randint(1, suma-1)
        self.strength = 10 + ran
        suma -= ran
        self.agility = suma + 10
        self.maxhealth = get_maxhealth(gamer)
        self.maxmana = 50
        self.mana = self.maxmana
        self.armor = self.level * 10
        self.health = self.maxhealth
        self.attack = self.strength * 0.9

    def __unicode__(self):
        return self.name


class MediumEnemy:
    def __init__(self, p):
        self.name = "Medium Enemy"
        self.classname = get_class()
        gamer = Player.objects.get(name=p)
        suma = gamer.strength + gamer.agility - 20
        self.level = gamer.level
        ran = randint(1, suma-1)
        self.strength = 10 + ran
        suma -= ran
        self.agility = suma + 10
        self.maxhealth = get_maxhealth(gamer)
        self.maxmana = 50
        self.mana = self.maxmana
        self.health = self.maxhealth
        self.armor = self.level * 10
        self.attack = self.strength * 0.9

    def __unicode__(self):
        return self.name


class HardEnemy:
    def __init__(self, p):
        self.classname = get_class()
        self.name = "Hard Enemy"
        gamer = Player.objects.get(name=p)
        suma = gamer.strength + gamer.agility - 10
        self.level = gamer.level
        ran = randint(1, suma-1)
        self.strength = 10 + ran
        suma -= ran
        self.agility = suma + 10
        self.maxhealth = get_maxhealth(gamer)
        self.maxmana = 50
        self.mana = self.maxmana
        self.health = self.maxhealth
        self.armor = self.level * 10
        self.attack = self.strength * 0.9

    def __unicode__(self):
        return self.name
