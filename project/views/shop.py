from project.models import ArmorItem, Player, Weapon
from django.shortcuts import render


def shop(request, p):
    gamer = Player.objects.get(pk=p)
    return render(request, 'shop/shop_items.html', {'armor': ArmorItem.objects.exclude(pk=1),
                                                    'weapon': Weapon.objects.all(), 'p': gamer})


def buy(request, p, i):

    gamer = Player.objects.get(pk=p)

    if 'Armor' in i:
        item = ArmorItem.objects.get(name=i)
        if item.requiredlv <= gamer.level and item.price <= gamer.gold:
            gamer.armorid = item
            gamer.gold -= item.price
            if gamer.bonus_health > 0:
                gamer.maxhealth -= gamer.bonus_health
            gamer.bonus_health = item.bonus_health
            gamer.maxhealth += gamer.bonus_health
            gamer.save()
            return render(request, 'shop/buy.html', {'msg': "Gratulacje! masz nowy armor.", 'p': p})
        else:
            return render(request, 'shop/buy.html', {'msg': "Masz za malo golda badz za maly level.", 'p': p})
    else:
        item = Weapon.objects.get(name=i)
        if item.requiredlv <= gamer.level and item.price <= gamer.gold:
            gamer.weapon_id = item
            gamer.gold -= item.price
            if gamer.bonus_attack > 0:
                gamer.attack -= gamer.bonus_attack
                gamer.agility -= gamer.bonus_agility
            gamer.bonus_attack = item.bonus_attack
            gamer.bonus_agility = item.bonus_agility
            gamer.agility += gamer.bonus_agility
            gamer.attack += gamer.bonus_attack
            gamer.save()
            return render(request, 'shop/buy.html', {'msg': "Gratulacje! masz nowa bron.", 'p': p})
        else:
            return render(request, 'shop/buy.html', {'msg': "Masz za malo golda badz za maly level.", 'p': p})


def reg(request, p, pay):
    gamer = Player.objects.get(pk=p)
    if int(pay) <= gamer.gold:
        gamer.health = gamer.maxhealth
        gamer.mana = gamer.maxmana
        gamer.gold -= int(pay)
        gamer.save()
        msg = "Zregenerowales sie !"
    else:
        msg = "Nie masz wystarczajacej ilosci gold"
    return render(request, 'shop/regen.html', {'p': p, 'msg': msg})
