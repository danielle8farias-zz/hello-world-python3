########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Programa retorna a latitude e a longitude do usuário
########

import requests
import json
from pprint import pprint

chave_api = 'u5eoJmS3s9PJ0X7RYCxrKWWaZm1WJhws'

#mandano uma requisição para o site indicado
requisicao1 = requests.get('http://www.geoplugin.net/json.gp')

#verificando o status do site (200 OK)
if requisicao1.status_code != 200:
    print('Não foi possível obter a localização.')
else:
    #r.text é do tipo string
    #json.loads retorna a string passada convertida em um dicionário
    localizacao = (json.loads(requisicao1.text))
    #pegando a chave geoplugin_latitude do dicionário localizacao
    latitude = localizacao['geoplugin_latitude']
    #pegando a chave geoplugin_longitude do dicionário localizacao
    longitude = localizacao['geoplugin_longitude']

    #url adaptava para usar as variáveis
    url_local_api = 'http://dataservice.accuweather.com/locations/v1/cities/geoposition/' \
    + 'search?apikey=' + chave_api \
    + '&q=' + latitude + '%2C%20' + longitude + '&language=pt-br'

    requisicao2 = requests.get(url_local_api)
    #verificando o status do site (200 OK)
    if requisicao2.status_code != 200:
        print('Não foi possível obter o código do local.')
    else:
        localizacao2 = (json.loads(requisicao2.text))
        #pprint imprime na tela o dicionário em um formato mais legível para humanos
        print(pprint(localizacao2))
