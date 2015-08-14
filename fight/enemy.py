from project.models import Player
from random import randint, random


class EasyEnemy:
    def __init__(self, p):
        self.name = "Easy Enemy"
        gamer = Player.objects.get(name=p)
        suma = gamer.strength + gamer.agility - 30
        self.level = gamer.level
        ran = randint(1, suma-1)
        self.strength = 10 + ran
        suma -= ran
        self.agility = suma + 10
        if random() > 0.5:
            if random() > 0.5:
                self.maxhealth = gamer.health + 20
            else:
                self.maxhealth = gamer.health + 10
        else:
            if random() > 0.5:
                self.maxhealth = gamer.health + 10
            else:
                self.maxhealth = gamer.health + 20
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
        gamer = Player.objects.get(name=p)
        suma = gamer.strength + gamer.agility - 20
        self.level = gamer.level
        ran = randint(1, suma-1)
        self.strength = 10 + ran
        suma -= ran
        self.agility = suma + 10
        if random() > 0.5:
            if random() > 0.5:
                self.maxhealth = gamer.health + 20
            else:
                self.maxhealth = gamer.health + 10
        else:
            if random() > 0.5:
                self.maxhealth = gamer.health + 10
            else:
                self.maxhealth = gamer.health + 20
        self.maxmana = 50
        self.mana = self.maxmana
        self.health = self.maxhealth
        self.armor = self.level * 10
        self.attack = self.strength * 0.9

    def __unicode__(self):
        return self.name


class HardEnemy:
    def __init__(self, p):
        self.name = "Hard Enemy"
        gamer = Player.objects.get(name=p)
        suma = gamer.strength + gamer.agility - 10
        self.level = gamer.level
        ran = randint(1, suma-1)
        self.strength = 10 + ran
        suma -= ran
        self.agility = suma + 10
        if random() > 0.5:
            if random() > 0.5:
                self.maxhealth = gamer.health + 20
            else:
                self.maxhealth = gamer.health + 10
        else:
            if random() > 0.5:
                self.maxhealth = gamer.health + 10
            else:
                self.maxhealth = gamer.health + 20
        self.maxmana = 50
        self.mana = self.maxmana
        self.health = self.maxhealth
        self.armor = self.level * 10
        self.attack = self.strength * 0.9

    def __unicode__(self):
        return self.name
