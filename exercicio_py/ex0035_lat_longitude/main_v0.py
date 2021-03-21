########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Programa retorna a latitude e a longitude do usuário através do IP dele.
########

import requests
import json
#from pprint import pprint

#mandano uma requisição para o site indicado
r = requests.get('http://www.geoplugin.net/json.gp')

#verificando o status do site (200 OK)
if r.status_code != 200:
    print('Não foi possível obter a localização.')
else:
    #r.text é do tipo string
    #json.loads retorna a string passada convertida em um dicionário
    localizacao = (json.loads(r.text))
    #pegando a chave geoplugin_latitude do dicionário localizacao
    latitude = localizacao['geoplugin_latitude']
    #pegando a chave geoplugin_longitude do dicionário localizacao
    longitude = localizacao['geoplugin_longitude']
    print(f'latitude: {latitude} \nlongitude: {longitude}')
    #pprint imprime na tela o dicionário em um formato mais legível para humanos
    #usado inicialmente apenas para pegar as chaves geoplugin_longitude e geoplugin_latitude
    #print(pprint(localizacao))
