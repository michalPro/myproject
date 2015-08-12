from django.contrib import admin
from .models import ArmorItem, Attack, Player


class ArmorItemsAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'requiredlv', 'price')
    search_fields = ('name', 'requiredlv', 'price')
    ordering = ['requiredlv']


class AttacksAdmin(admin.ModelAdmin):
    list_display = ('name', 'requiredlv', 'bonusattack', 'requiredmana')
    ordering = ('-requiredlv',)
    #raw_id_fields = ('publisher',)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'strength', 'agility', 'health', 'mana', 'experience', 'requiredexp', 'level',
                    'pointstoadd', 'actualarmorvalue', 'armorid')


admin.site.register(ArmorItem, ArmorItemsAdmin)
admin.site.register(Attack, AttacksAdmin)
admin.site.register(Player, PlayerAdmin)