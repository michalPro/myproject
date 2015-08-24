from project.models import ArmorItem, Player
from django.shortcuts import render


def shop(request, p):
    gamer = Player.objects.get(pk=p)
    return render(request, 'shop/shop_items.html', {'items': ArmorItem.objects.exclude(pk=1), 'p': p})


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
