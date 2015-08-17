import os


def populate():
    add_armor('Default', 5, 1, 0)
    add_armor('Leather Armor', 20, 3, 15)
    add_armor('Plate Armor', 45, 5, 60)
    add_armor('Chain Armor', 105, 12, 340)
    add_armor('Scale Armor', 200, 20, 1000)

    add_attack('Powerful Attack', 3, 1.2, 5)
    add_attack('Bleed', 5, 0.6, 8)
    add_attack('Double Attack', 8, 0.9, 15)
    add_attack('Powerful Attack', 15, 2.0, 40)

    add_class('Warrior')
    add_class('Thief')
    add_class('Tankozord')

    add_enemy('Easy Enemy', 1, 1, 1, 1, 1, 1, 1, 1, 1)
    add_enemy('Medium Enemy', 1, 1, 1, 1, 1, 1, 1, 1, 1)
    add_enemy('Hard Enemy', 1, 1, 1, 1, 1, 1, 1, 1, 1)

    # Print out what we have added to the user.
    for c in ArmorItem.objects.all():
        print c
    for t in Attack.objects.all():
        print t
    for c in ClassName.objects.all():
        print c
    for e in Enemy.objects.all():
        print e


def add_enemy(name, level, strength, agility, maxhealth, health, maxmana, mana, armor, attack):
    classname = ClassName.objects.get(name='Warrior')
    ae = Enemy.objects.get_or_create(name=name, level=level, attack=attack, maxmana=maxmana, maxhealth=maxhealth,
                                     strength=strength, agility=agility, health=health, mana=mana, armor=armor,
                                     classname=classname)
    return ae


def add_armor(name, value, requiredlv, price):
    ar = ArmorItem.objects.get_or_create(name=name, value=value, requiredlv=requiredlv, price=price)
    return ar


def add_attack(name, requiredlv, bonusattack, requiredmana):
    at = Attack.objects.get_or_create(name=name, requiredlv=requiredlv, bonusattack=bonusattack,
                                      requiredmana=requiredmana)
    return at


def add_class(name):
    ac = ClassName.objects.get_or_create(name=name)
    return ac

# Start execution here!
if __name__ == '__main__':
    print "Adding records to database.."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    from project.models import ArmorItem, Attack, ClassName, Enemy
    populate()
