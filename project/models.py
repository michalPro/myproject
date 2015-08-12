from django.db import models


class ArmorItem(models.Model):
    name = models.CharField(max_length=30)
    value = models.IntegerField()
    requiredlv = models.IntegerField()
    price = models.IntegerField()

    def __unicode__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=40)
    level = models.IntegerField()
    experience = models.IntegerField()
    requiredexp = models.IntegerField()
    strength = models.IntegerField()
    agility = models.IntegerField()
    health = models.IntegerField()
    attack = models.IntegerField()
    mana = models.IntegerField()
    pointstoadd = models.IntegerField()
    armorid = models.ForeignKey(ArmorItem)
    actualarmorvalue = models.IntegerField()
    gold = models.IntegerField()

    def __unicode__(self):
        return self.name

    def __init__(self, name):
        self.name = name
        self.strength = 25
        self.agility = 25
        self.attack = 20
        self.experience = 0
        self.health = 200
        self.level = 1
        self.mana = 50
        self.pointstoadd = 20
        self.requiredexp = 100
        self.gold = 20


class Attack(models.Model):
    name = models.CharField(max_length=50)
    requiredlv = models.IntegerField()
    bonusattack = models.DecimalField(max_digits=4, decimal_places=2)
    requiredmana = models.IntegerField()

    def __unicode__(self):
        return self.name
