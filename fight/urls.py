from django.conf.urls import include, url
import fight.views as views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^arenalevel/(?P<e>[A-Za-z\s]+)$', views.arenalevel),
]
