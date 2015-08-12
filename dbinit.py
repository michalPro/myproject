import os


def populate():
    add_armor('Leather Armor', 20, 1, 15)
    add_armor('Plate Armor', 45, 5, 60)
    add_armor('Chain Armor', 105, 12, 340)
    add_armor('Scale Armor', 200, 20, 1000)

    add_attack('Powerful Attack', 3, 1.2, 5)
    add_attack('Bleed', 5, 0.6, 8)
    add_attack('Double Attack', 8, 0.9, 15)
    add_attack('Powerful Attack', 15, 2.0, 40)

    # Print out what we have added to the user.
    for c in ArmorItem.objects.all():
        print c
    for t in Attack.objects.all():
        print t


def add_armor(name, value, requiredlv, price):
    ar = ArmorItem.objects.get_or_create(name=name, value=value, requiredlv=requiredlv, price=price)
    return ar


def add_attack(name, requiredlv, bonusattack, requiredmana):
    at = Attack.objects.get_or_create(name=name, requiredlv=requiredlv, bonusattack=bonusattack,
                                      requiredmana=requiredmana)
    return at

# Start execution here!
if __name__ == '__main__':
    print "Adding records to database.."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    from project.models import ArmorItem, Attack
    populate()
