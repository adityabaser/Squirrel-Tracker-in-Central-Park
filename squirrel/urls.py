from django.urls import path

from . import views

urlpatterns = [
            path('sightings/',views.sighting_list, name='sighting_list'),
            path('map/',views.sighting_map, name='sighting_map'),
            path('add/',views.sighting_add, name='sighting_add'),
            path('', views.index, name='index'),
            ]
