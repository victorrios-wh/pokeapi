from django.conf.urls import include, url
from django.contrib import admin
from .views import index

urlpatterns = [
    # Examples:
    # url(r'^$', 'pokeapi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    url(r'^pokemon/', include('apps.pokemon.urls', namespace='pokemon'))
]
