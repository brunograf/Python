import requests
from pprint import pprint

api_key = '78ff3f93346440e0a9b203504261706'
link_api = 'http://api.weatherapi.com/v1/current.json'
parametros = {
    'key': api_key,
    'q': 'Joinville',
    'lang': 'pt'
}

resposta = requests.get(link_api, params = parametros)

if resposta.status_code == 200:
    dados = resposta.json()
    pprint(dados)
    print(f"Temperatura atual em {dados['location']['name']}: {dados['current']['temp_c']}°C")