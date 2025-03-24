import requests

API_CONFIG = {
    'GET_LIST_POKEMON': {
        'method': 'GET',
        'url': 'https://pokeapi.co/api/v2/pokemon/',
        'headers': { 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Code Club' },
        'data': 'query'
    },
    'GET_CUSTOM_URL': {
        'method': 'GET',
        'headers': { 
            'Content-Type': 'application/json; charset=utf-8',
            'User-Agent': 'Code-Club',
            'Accept': '*/*',
            'access-control-allow-origin': '*'
        },
        'data': 'query'
    }
}

def call_api(api, args={}, headers={}, url=''):
    """
    Ejecuta el llamado a un api configurado en API_CONFIG

    Args:
        api (str) nombre del valor en diccionario API_CONFIG
        args (dict) valor opcional con la data (query/body) para el llamado
        headers (dict) valor opcional con los headers a agregar al llamado
        url (str) valor opcional que sobreescribe la url configurada en el diccionario API_CONFIG

    Returns:
        dict con las siguientes propiedades:
            success (bool) indica si se completo el llamado
            status (int) indica el status_code del llamado o 500
            response (dict) response json del llamado o None
    """
    result = { 'success': False, 'status': 500, 'response': None }

    if API_CONFIG.get(api):
        api_config = API_CONFIG[api]
    else:
        return result
    
    if headers:
        api_config['headers'].update(headers)

    if url:
        api_config['url'] = url

    if api_config['data'] == 'query':
        response = requests.request(api_config['method'], api_config['url'], params=args, headers=api_config['headers'])
    elif api_config['data'] == 'body':
        response = requests.request(api_config['method'], api_config['url'], json=args, headers=api_config['headers'])

    if response.ok:
        result.update({
            'success': True,
            'status': response.status_code,
            'response': response.json()
        })
    else:
        print('Error al llamar api: {}'.format(response.url))

    return result