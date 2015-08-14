from django.conf.urls import include, url
import player.views as views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index),
]
