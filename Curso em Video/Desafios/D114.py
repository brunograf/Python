import requests

try:
    site = requests.get('https://pudim.com.br')
except:
    print('O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')