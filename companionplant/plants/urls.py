from django.conf.urls import patterns, url

from plants import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<plant_id>\d+)/$', views.plant, name='plant'),
    url(r'^add/', views.addMatch, name='addMatch'),
    url(r'^create', views.createMatch, name='createMatch')
)