from django.conf.urls import include, url
import fight.views as views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^arena/(?P<p>[A-Za-z0-9\s]+)/(?P<e>[A-Za-z\s]+)$', views.arena),
]
