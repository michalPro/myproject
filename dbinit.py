import os


def populate():
    add_armor('Default', 5, 10, 1, 0)
    add_armor('Leather Armor', 20, 30, 3, 500)
    add_armor('Plate Armor', 95, 80, 5, 1000)
    add_armor('Chain Armor', 264, 160, 12, 5000)
    add_armor('Scale Armor', 500, 300, 20, 15000)

    add_attack('Standard Attack', 1, 1.0, 0)
    add_attack('Boomerang Attack', 3, 1.2, 5)
    add_attack('Bleed', 5, 0.6, 8)
    add_attack('Double Attack', 8, 0.9, 15)
    add_attack('Powerful Attack', 15, 2.0, 40)

    add_class('Warrior')
    add_class('Thief')
    add_class('Tankozord')

    add_enemy('Easy Enemy', 1, 1, 1, 1, 1, 1, 1, 1, 1)
    add_enemy('Medium Enemy', 1, 1, 1, 1, 1, 1, 1, 1, 1)
    add_enemy('Hard Enemy', 1, 1, 1, 1, 1, 1, 1, 1, 1)

    add_weapon("Short Sword", 5, 3, 2, 150)
    add_weapon("Long Sword", 15, 7, 7, 1600)
    add_weapon("Two Handed Sword", 25, 12, 14, 7000)
    add_weapon("DragonSlayer Sword", 40, 20, 22, 20000)

    clasname = ClassName.objects.get(name='Tankozord')
    arm = ArmorItem.objects.get(pk=1)

    add_player("Lv1", 300, clasname, arm, 1)
    add_player("Lv3", 5000, clasname, arm, 3)
    add_player("Lv5", 15000, clasname, arm, 5)
    add_player("Lv8", 25000, clasname, arm, 8)
    add_player("Lv13", 30000, clasname, arm, 13)
    add_player("Lv15", 35000, clasname, arm, 15)
    add_player("Lv20", 40000, clasname, arm, 20)
    add_player("Lv22", 55000, clasname, arm, 22)


    # Print out what we have added to the user.
    for c in ArmorItem.objects.all():
        print c
    for t in Attack.objects.all():
        print t
    for c in ClassName.objects.all():
        print c
    for e in Enemy.objects.all():
        print e
    for w in Weapon.objects.all():
        print w
    for p in Player.objects.all():
        print p


def add_enemy(name, level, strength, agility, maxhealth, health, maxmana, mana, armor, attack):
    classname = ClassName.objects.get(name='Warrior')
    ae = Enemy.objects.get_or_create(name=name, level=level, attack=attack, maxmana=maxmana, maxhealth=maxhealth,
                                     strength=strength, agility=agility, health=health, mana=mana, armor=armor,
                                     classname=classname)
    return ae


def add_armor(name, value, bonus_health, requiredlv, price):
    ar = ArmorItem.objects.get_or_create(name=name, value=value, requiredlv=requiredlv, price=price,
                                         bonus_health=bonus_health)
    return ar


def add_weapon(name, bonus_attack, bonus_agility, requiredlv, price):
    ar = Weapon.objects.get_or_create(name=name, bonus_attack=bonus_attack, bonus_agility=bonus_agility,
                                         requiredlv=requiredlv, price=price)
    return ar


def add_attack(name, requiredlv, bonusattack, requiredmana):
    aw = Attack.objects.get_or_create(name=name, requiredlv=requiredlv, bonusattack=bonusattack,
                                      requiredmana=requiredmana)
    return aw


def add_class(name):
    ac = ClassName.objects.get_or_create(name=name)
    return ac


def add_player(name, gold, classname, armorid, level):
    maxhp = 180+50*level
    maxma = 45+5*level
    ag = 20+5*level
    st = 29+6*level
    at = int(round(float(st) * 0.9, 0))
    p = Player.objects.get_or_create(name=name, strength=st, agility=ag, maxhealth=maxhp, maxmana=maxma, experience=0,
                        requiredexp=400, level=level, gold=gold, classname=classname, attack=at,
                        armorid=armorid, isarmordamaged=False, health=maxhp, mana=maxma, bonus_attack=0, bonus_agility=0,
                        bonus_health=0)
    return p

# Start execution here!
if __name__ == '__main__':
    print "Adding records to database.."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    from project.models import ArmorItem, Attack, ClassName, Enemy, Player, Weapon
    populate()
