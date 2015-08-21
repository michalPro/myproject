from project.models import ArmorItem, Player
from django.shortcuts import render


def shop(request, p):
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
