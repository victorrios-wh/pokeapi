from utils import call_api

def get_pokemon_info(args={}):
    
    if args:
        args = args
    else:
        args = { 'limit': 5 }
    
    #se hace llamado para obtener los nombres y url de los pokemon
    result_list = call_api('GET_LIST_POKEMON', args)
    if result_list['success'] and result_list['status'] == 200:
        #se obtuvieron datos

        #se reduce la informacion en la variable para manejar mejor la informacion a insertar
        pokemon_list = result_list['response']['results']
        for pokemon in pokemon_list:
            #por cada pokemon se obtiene el detalle
            result_info = call_api('GET_CUSTOM_URL', url=pokemon['url'])
            if result_info['success'] and result_info['status'] == 200:
                #se obtuvo detalle

                result_info = result_info['response']

                #se agregan datos al pokemon
                pokemon.update({
                    'name': pokemon['name'].upper(),
                    'img': result_info['sprites']['front_default'],
                    'weight': result_info['weight'],
                    'height': result_info['height'],
                    'main_type': result_info['types'][0]['type']['name'],
                    'second_type': result_info['types'][1]['type']['name'] if len(result_info['types']) > 1 else None,
                    'abilities': result_info['abilities'],
                    'moves': result_info['moves']
                })
                for move in pokemon['moves']:
                    del move['version_group_details']
                
            else:
                print('No se obtuvo informacion de pokemon')

        return result_list
    else:
        print('No se obtuvo informacion de pokemon')
        return {}
    
def get_pokemon_by_type(type):

    url = 'https://pokeapi.co/api/v2/type/{}'.format(type)
    #se hace llamado para obtener los nombres y url de los pokemon
    result_list = call_api('GET_CUSTOM_URL', url=url)
    if result_list['success'] and result_list['status'] == 200:
        #se obtuvieron datos
        
        #se reduce la informacion en la variable para manejar mejor la informacion a insertar
        pokemon_list = result_list['response']['pokemon']
        del result_list['response']
        result_list['response']={ 'results':[] }
        for pokemon in pokemon_list:
            
            #por cada pokemon se obtiene el detalle
            result_info = call_api('GET_CUSTOM_URL', url=pokemon['pokemon']['url'])
            if result_info['success'] and result_info['status'] == 200:
                #se obtuvo detalle

                result_info = result_info['response']

                #se elimina informacion innecesaria
                for move in result_info['moves']:
                    del move['version_group_details']

                #se agregan datos al pokemon
                result_list['response']['results'].append({
                    'name': pokemon['pokemon']['name'].upper(),
                    'img': result_info['sprites']['front_default'],
                    'weight': result_info['weight'],
                    'height': result_info['height'],
                    'main_type': result_info['types'][0]['type']['name'],
                    'second_type': result_info['types'][1]['type']['name'] if len(result_info['types']) > 1 else None,
                    'abilities': result_info['abilities'],
                    'moves': result_info['moves']
                })
                
            else:
                print('No se obtuvo informacion de pokemon: {}'.format(pokemon['pokemon']['name'].upper()))

        return result_list
    else:
        print('No se obtuvo informacion de pokemon')
        return {}

