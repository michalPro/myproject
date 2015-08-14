from django.shortcuts import render
from fight.enemy import EasyEnemy, HardEnemy, MediumEnemy

# Create your views here.


def index(request, p):
    ee = EasyEnemy(p)
    me = MediumEnemy(p)
    he = HardEnemy(p)
    return render(request, 'fight/arenalevel.html', {'p': p, 'ee': ee, 'me': me, 'he': he})


def arena(request, p, e):
    if e == "Easy Enemy":
        e = EasyEnemy(p)
    elif e == "Medium Enemy":
        e = MediumEnemy(p)
    else:
        e = HardEnemy(p)
    return render(request, 'fight/arena.html', {'p': p, 'e': e})
