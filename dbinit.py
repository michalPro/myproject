import os


def populate():
    add_armor('Default', 10, 30, 1, 0)
    add_armor('Leather Armor', 35, 150, 3, 500)
    add_armor('Plate Armor', 100, 400, 6, 1000)
    add_armor('Chain Armor', 400, 850, 12, 120000)
    add_armor('Scale Armor', 1000, 2000, 20, 20000000)

    add_attack('Standard Attack', 1, 1.0, 0)
    add_attack('Boomerang Attack', 3, 1.5, 5)
    add_attack('Bleed', 5, 0.5, 8)
    add_attack('Double Attack', 8, 1.2, 25)
    add_attack('Powerful Attack', 15, 3.0, 40)

    add_class('Warrior')
    add_class('Thief')
    add_class('Tankozord')

    add_enemy('Easy Enemy', 1, 1, 1, 1, 1, 1, 1, 1, 1)
    add_enemy('Medium Enemy', 1, 1, 1, 1, 1, 1, 1, 1, 1)
    add_enemy('Hard Enemy', 1, 1, 1, 1, 1, 1, 1, 1, 1)
    add_enemy('Easy Boss', 10, 100, 60, 1000, 1000, 200, 200, 200, 100)
    add_enemy('Medium Boss', 15, 150, 120, 3500, 3500, 400, 400, 500, 200)
    add_enemy('Hard Boss', 20, 200, 180, 10000, 10000, 800, 800, 1000, 300)


    add_weapon("Short Sword", 5, 3, 2, 150)
    add_weapon("Long Sword", 25, 15, 7, 5500)
    add_weapon("Two Handed Sword", 55, 40, 14, 320000)
    add_weapon("DragonSlayer Sword", 110, 80, 22, 60000000)

    clasname = ClassName.objects.get(name='Tankozord')
    arm = ArmorItem.objects.get(pk=1)

    add_player("Lv1", 300, clasname, arm, 1)
    add_player("Lv3", 5000, clasname, arm, 3)
    add_player("Lv5", 150000, clasname, arm, 5)
    add_player("Lv8", 250000, clasname, arm, 8)
    add_player("Lv13", 30000000, clasname, arm, 13)
    add_player("Lv15", 350000000, clasname, arm, 15)
    add_player("Lv20", 400000000, clasname, arm, 20)
    add_player("Lv22", 550000000, clasname, arm, 22)

    add_elixir("Small Elixir", 25, 25, 1, 0.01)
    add_elixir("Medium Elixir", 40, 40, 2, 0.02)
    add_elixir("Big Elixir", 65, 65, 4, 0.04)
    add_elixir("Ultimate Elixir", 100, 100, 8, 0.08)


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
    for e in Elixir.objects.all():
        print e


def add_enemy(name, level, strength, agility, maxhealth, health, maxmana, mana, armor, attack):
    ae = Enemy.objects.get_or_create(name=name, level=level, attack=attack, maxmana=maxmana, maxhealth=maxhealth,
                                     strength=strength, agility=agility, health=health, mana=mana, armor=armor,
                                     dot_damage=0, dot_rounds=0)
    return ae


def add_elixir(name, health_restore, mana_restore, price, multiplier):
    ae = Elixir.objects.get_or_create(name=name, health_restore=health_restore, mana_restore=mana_restore,
                                      price=price, multiplier=multiplier)
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
    exp = 400
    at = int(round(float(st) * 0.9, 0))
    for x in range(0, level):
        exp *= 2
    p = Player.objects.get_or_create(name=name, strength=st, agility=ag, maxhealth=maxhp, maxmana=maxma, experience=0,
                        requiredexp=exp, level=level, gold=gold, classname=classname, attack=at,
                        armorid=armorid, isarmordamaged=False, health=maxhp, mana=maxma, bonus_attack=0, bonus_agility=0,
                        bonus_health=0, dot_damage=0, dot_rounds=0, small_elixir=0, medium_elixir=0, big_elixir=0,
                                     ultimate_elixir=0)
    return p

# Start execution here!
if __name__ == '__main__':
    print "Adding records to database.."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    from project.models import ArmorItem, Attack, ClassName, Enemy, Player, Weapon, Elixir
    populate()
