from django.conf.urls import include, url
import project.views.start as menu

urlpatterns = [
    url(r'^menu/$', menu.start),
    url(r'^load/$', menu.load),
    url(r'^create/$', menu.createnew),
    url(r'^player/(?P<p>[A-Za-z]+)', menu.player),
]
