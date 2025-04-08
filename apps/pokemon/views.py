from django.shortcuts import render
from .utils import get_pokemon_by_type, get_pokemon_info

# Create your views here.
def pokemon_list(request):
    result_list = get_pokemon_info(request.GET)

    #guardar lista en session
    request.session['list'] = result_list

    if result_list['success'] and result_list['status'] == 200:
        #se obtuvieron datos
        pokemon_list = result_list['response']['results']

    contexto = {
        'title': 'Lista pokemon',
        'next': result_list['response']['next'],
        'prev': result_list['response']['previous'],
        'pokemons': pokemon_list
    }
    return render(request, 'pokemon/index.html', contexto)

def pokemon_detail(request, name):
    for pokemon in request.session['list']['response']['results']:
        if pokemon['name'] == name:
            detail = pokemon
            break

    contexto = {
        'pokemon': detail
    }
    return render(request, 'pokemon/detail.html', contexto)

def pokemon_list_by_type(request, type):
    if request.GET:
        args = request.GET
    else:
        args = { 'limit': 5, 'offset': 0 }

    result_list = get_pokemon_by_type(type, args)

    #guardar lista en session
    request.session['list'] = result_list

    if result_list['success'] and result_list['status'] == 200:
        #se obtuvieron datos
        pokemon_list = result_list['response']['results']

    contexto = {
        'title': 'Lista pokemon tipo: {}'.format(type),
        'type': type,
        'pokemons': pokemon_list,
        'next': result_list['response']['next'],
        'prev': result_list['response']['previous']

    }
    return render(request, 'pokemon/index.html', contexto)