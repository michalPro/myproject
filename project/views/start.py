# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, RequestContext, redirect
from project.models import ArmorItem, Attack, Player, ClassName
from django.shortcuts import HttpResponseRedirect
from project.formm import CreateForm


def start(request):
    return render(request, 'menu/start.html')


def createnew(request):
    if request.method == "POST":
        choice = request.POST.get("choice", "")
        name = request.POST.get("name", "")
        aid = ArmorItem.objects.get(name="Default")
        classname = ClassName.objects.get(name=choice)
        if choice == "Warrior":
            p = Player(name=name, strength=35, agility=30, health=250, mana=50, experience=0,
                        requiredexp=100, level=1, gold=20, classname=classname, attack=20,
                        armorid=aid, isarmordamaged=False)
            p.save()
            return HttpResponseRedirect('/menu/player/%s/' % p)
        elif choice == "Thief":
            p = Player(name=name, strength=30, agility=37, health=230, mana=50, experience=0,
                        requiredexp=100, level=1, gold=20, classname=classname, attack=20,
                        armorid=aid, isarmordamaged=False)
            p.save()
            return HttpResponseRedirect('/menu/player/%s/' % p)
        else: #choice == "Tankozord"
            p = Player(name=name, strength=35, agility=25, health=300, mana=50, experience=0,
                        requiredexp=100, level=1, gold=20, classname=classname, attack=20,
                        armorid=aid, isarmordamaged=False)
            p.save()
            return HttpResponseRedirect('/menu/player/%s/' % p)
    else:
        #form = CreateForm
        return render(request, 'menu/createnew.html')


def load(request):
    plist = Player.objects.all()
    return render(request, 'menu/load.html', {'players': plist})


def player(request, p):
    gamer = Player.objects.get(name=p)
    return render(request, 'menu/player.html', {'p': gamer})
