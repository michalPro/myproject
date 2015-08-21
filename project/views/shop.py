from project.models import ArmorItem, Player
from django.shortcuts import render


def shop(request, p):
    gamer = Player.objects.get(pk=p)
    gold_to_pay = round((float(gamer.maxhealth) - float(gamer.health))/25.0 + (float(gamer.maxmana) - float(gamer.mana))/10.0, 0)
    return render(request, 'shop/shop_items.html', {'items': ArmorItem.objects.exclude(pk=1), 'p': p, 'pay': int(gold_to_pay)})


def buy(request, p, i):
    item = ArmorItem.objects.get(name=i)
    gamer = Player.objects.get(pk=p)
    if item.requiredlv <= gamer.level and item.price <= gamer.gold:
        gamer.armorid = item
        gamer.gold -= item.price
        gamer.save()
        return render(request, 'shop/buy.html', {'msg': "Gratulacje! masz nowy armor.", 'p': p})
    else:
        return render(request, 'shop/buy.html', {'msg': "Masz za malo golda badz za maly level.", 'p': p})


def reg(request, p):
    gamer = Player.objects.get(pk=p)
    gold_to_pay = round((float(gamer.maxhealth) - float(gamer.health))/25.0 + (float(gamer.maxmana) - float(gamer.mana))/10.0, 0)
    if gold_to_pay <= gamer.gold:
        gamer.health = gamer.maxhealth
        gamer.mana = gamer.maxmana
        gamer.gold -= gold_to_pay
        gamer.save()
        msg = "Zregenerowales sie !"
    else:
        msg = "Nie masz wystarczajacej ilosci gold"
    return render(request, 'shop/regen.html', {'p': p, 'msg': msg})

