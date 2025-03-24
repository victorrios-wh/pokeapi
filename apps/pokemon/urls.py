from django.conf.urls import url
from .views import pokemon_detail, pokemon_list, pokemon_list_by_type 

urlpatterns = [
    url(r'^$', pokemon_list, name="list"),
    url(r'^(?P<type>[\w\-]+)/$', pokemon_list_by_type, name="list_type"),
    url(r'^detalle/(?P<name>[\w\-]+)/', pokemon_detail, name='detail'),
]
