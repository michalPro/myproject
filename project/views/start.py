# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, RequestContext, redirect
from project.models import ArmorItem, Attack, Player, ClassName
from django.shortcuts import HttpResponseRedirect, HttpResponse


def start(request):
    return render(request, 'menu/start.html')


def createnew(request):
    if request.method == "POST":
        choice = request.POST.get("choice", "")
        name = request.POST.get("name", "")
        aid = ArmorItem.objects.get(name="Default")
        classname = ClassName.objects.get(name=choice)
        if choice == "Warrior":
            p = Player(name=name, strength=35, agility=30, maxhealth=250, maxmana=50, experience=0,
                        requiredexp=400, level=1, gold=20, classname=classname, attack=20,
                        armorid=aid, isarmordamaged=False, health=250, mana=50, bonus_attack=0, bonus_agility=0,
                        bonus_health=0)
            p.attack = p.strength * 0.9
            p.save()
            return HttpResponseRedirect('/player/%s/' % p.id)
        elif choice == "Thief":
            p = Player(name=name, strength=30, agility=37, maxhealth=230, maxmana=50, experience=0,
                        requiredexp=400, level=1, gold=20, classname=classname, attack=20,
                        armorid=aid, isarmordamaged=False, health=230, mana=50, bonus_attack=0, bonus_agility=0,
                        bonus_health=0)
            p.attack = p.strength * 0.9
            p.save()
            return HttpResponseRedirect('/player/%s/' % p.id)
        else: #choice == "Tankozord"
            p = Player(name=name, strength=35, agility=25, maxhealth=300, maxmana=50, experience=0,
                        requiredexp=400, level=1, gold=20, classname=classname, attack=20,
                        armorid=aid, isarmordamaged=False, health=300, mana=50, bonus_attack=0, bonus_agility=0,
                        bonus_health=0)
            p.attack = p.strength * 0.9
            p.save()
            return HttpResponseRedirect('/player/%s/' % p.id)
    else:
        return render(request, 'menu/createnew.html')


def load(request):
    plist = Player.objects.all()
    return render(request, 'menu/load.html', {'players': plist})

