from project.models import ArmorItem, Player, Weapon
from django.shortcuts import render


def shop(request, p):
    gamer = Player.objects.get(pk=p)
    return render(request, 'shop/shop_items.html', {
        'armor': ArmorItem.objects.exclude(pk=1),
        'weapon': Weapon.objects.all(), 'p': gamer,
    })


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
            return render(request, 'shop/buy.html', {
                'msg': "Gratulacje! masz nowy armor.", 'p': p
            })
        else:
            return render(request, 'shop/buy.html', {
                'p': p
            })
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
            return render(request, 'shop/buy.html', {
                'msg': "Gratulacje! masz nowa bron.",
                'p': p
            })
        else:
            return render(request, 'shop/buy.html', {'msg': "Masz za malo golda badz za maly level.", 'p': p})


def reg(request):

    gamer = Player.objects.get(name=request.GET['p'])
    gold_to_pay = int(round(((float(gamer.maxhealth) - float(gamer.health))/10.0
                             + (float(gamer.maxmana) - float(gamer.mana))/5.0) * (float(gamer.level)), 0))
    if int(gold_to_pay) <= gamer.gold:
        gamer.health = gamer.maxhealth
        gamer.mana = gamer.maxmana
        gamer.gold -= int(gold_to_pay)
        gamer.save()
        gold_to_pay = 0

    return render(request, 'shop/regen.html', {
        'p': gamer,
        'armor': ArmorItem.objects.get(name=gamer.armorid).value,
        'pay': int(gold_to_pay),
        'health': gamer.health * 100 / gamer.maxhealth,
        'mana': gamer.mana * 100 / gamer.maxmana,
    })
