from project.models import ArmorItem, Player, Weapon, Elixir
from django.shortcuts import render, HttpResponse


def shop(request, p):
    gamer = Player.objects.get(pk=p)
    return render(request, 'shop/shop_items.html', {
        'armor': ArmorItem.objects.exclude(pk=1),
        'weapon': Weapon.objects.all(),
        'p': gamer,
    })


def alchemist(request, p):
    gamer = Player.objects.get(pk=p)
    for elixir in Elixir.objects.all():
        elixir.price = (gamer.requiredexp / gamer.level) * elixir.multiplier
        elixir.save()
    return render(request, 'shop/alchemist.html', {
        'elixirs': Elixir.objects.all(),
        'p': gamer,
    })


def buy_elixir(request):
    gamer = Player.objects.get(name=request.GET['p'])
    i = Elixir.objects.get(name=request.GET['i'])
    if i.price <= gamer.gold:
        if i.name == 'Small Elixir':
            gamer.small_elixir += 1
            gamer.gold -= i.price
        elif i.name == 'Medium Elixir':
            gamer.medium_elixir += 1
            gamer.gold -= i.price
        elif i.name == 'Big Elixir':
            gamer.big_elixir += 1
            gamer.gold -= i.price
        else:
            gamer.ultimate_elixir += 1
            gamer.gold -= i.price
        gamer.save()
    return render(request, 'shop/elixir.html', {
        'p': gamer,
        'elixirs': Elixir.objects.all(),
    })


def buy(request):

    gamer = Player.objects.get(name=request.GET['p'])
    i = request.GET['i']

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
        'p': gamer,
        'armor': ArmorItem.objects.exclude(pk=1),
        'weapon': Weapon.objects.all(),
    })


def reg(request):

    gamer = Player.objects.get(name=request.GET['p'])
    gold_to_pay = int(float(gamer.health)/float(gamer.maxhealth) *
                      (float(gamer.requiredexp) / float(gamer.level)) * 0.01)
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
