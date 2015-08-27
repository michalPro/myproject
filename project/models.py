from django.db import models


class ArmorItem(models.Model):
    name = models.CharField(max_length=30)
    value = models.IntegerField()
    bonus_health = models.IntegerField()
    requiredlv = models.IntegerField()
    price = models.IntegerField()

    def __unicode__(self):
        return self.name


class Weapon(models.Model):
    name = models.CharField(max_length=30)
    bonus_attack = models.IntegerField()
    bonus_agility = models.IntegerField()
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
    bonus_attack = models.IntegerField()
    bonus_agility = models.IntegerField()
    bonus_health = models.IntegerField()
    isarmordamaged = models.BooleanField()
    gold = models.IntegerField()
    dot_damage = models.IntegerField()
    dot_rounds = models.IntegerField()
    small_elixir = models.IntegerField()
    medium_elixir = models.IntegerField()
    big_elixir = models.IntegerField()
    ultimate_elixir = models.IntegerField()

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
    dot_damage = models.IntegerField()
    dot_rounds = models.IntegerField()

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
    player_attack_name = models.CharField(max_length=40)
    enemy_attack_name = models.CharField(max_length=40)
    player_bonus_attack = models.IntegerField()
    enemy_bonus_attack = models.IntegerField()


class Elixir(models.Model):
    name = models.CharField(max_length=40)
    health_restore = models.IntegerField()
    mana_restore = models.IntegerField()
    price = models.IntegerField()
    multiplier = models.DecimalField(max_digits=4, decimal_places=2)

    def __unicode__(self):
        return self.name
