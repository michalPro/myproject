from django.db import models


class ArmorItem(models.Model):
    name = models.CharField(max_length=30)
    value = models.IntegerField()
    requiredlv = models.IntegerField()
    price = models.IntegerField()

    def __unicode__(self):
        return self.name


class ClassName(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=40)
    level = models.IntegerField()
    experience = models.IntegerField()
    requiredexp = models.IntegerField()
    strength = models.IntegerField()
    agility = models.IntegerField()
    maxhealth = models.IntegerField()
    health = models.IntegerField()
    attack = models.IntegerField()
    maxmana = models.IntegerField()
    mana = models.IntegerField()
    classname = models.ForeignKey(ClassName)
    armorid = models.ForeignKey(ArmorItem)
    isarmordamaged = models.BooleanField()
    gold = models.IntegerField()

    def __unicode__(self):
        return self.name


class Enemy(models.Model):
    name = models.CharField(max_length=15)
    level = models.IntegerField()
    strength = models.IntegerField()
    agility = models.IntegerField()
    maxhealth = models.IntegerField()
    health = models.IntegerField()
    attack = models.IntegerField()
    maxmana = models.IntegerField()
    mana = models.IntegerField()
    classname = models.ForeignKey(ClassName)
    armor = models.IntegerField()

    def __unicode__(self):
        return self.name


class Attack(models.Model):
    name = models.CharField(max_length=50)
    requiredlv = models.IntegerField()
    bonusattack = models.DecimalField(max_digits=4, decimal_places=2)
    requiredmana = models.IntegerField()

    def __unicode__(self):
        return self.name


class AttackLog(models.Model):
    enemydamage = models.IntegerField()
    playerdamage = models.IntegerField()
