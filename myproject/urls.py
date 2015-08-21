"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from project.views.views_fight import player_attack, enemy_attack, \
    partial_view_enemy, partial_view_player, partial_view_console_log, console_log, victory
from project.views.shop import shop, buy
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^attack/$', player_attack),
    url(r'^console_log/$', console_log),
    url(r'^response/$', enemy_attack),
    url(r'^enemy/$', partial_view_enemy),
    url(r'^console/$', partial_view_console_log),
    url(r'^player/$', partial_view_player),
    url(r'^victory/$', victory),
    url(r'^menu/', include('project.urls', namespace='menu')),
    url(r'^player/(?P<p>[0-9]+)/', include('player.urls', namespace='player')),
    url(r'^player/(?P<p>[0-9]+)/shop/$', shop),
    url(r'^player/(?P<p>[0-9]+)/shop/buy/(?P<i>[\sA-Za-z]+)$', buy),
    url(r'^player/(?P<p>[0-9]+)/arena/', include('fight.urls', namespace='fight')),
]

