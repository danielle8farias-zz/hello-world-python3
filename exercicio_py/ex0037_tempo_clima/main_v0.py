########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Programa retorna o tempo e temperatura da localidade do usuário
########

import requests
import json
from pprint import pprint

chave_api = 'u5eoJmS3s9PJ0X7RYCxrKWWaZm1WJhws'

#mandano uma requisição para o site indicado
requisicao_geoplugin = requests.get('http://www.geoplugin.net/json.gp')

#verificando o status do site (200 OK)
if requisicao_geoplugin.status_code != 200:
    print('Não foi possível obter a localização.')
else:
    #r.text é do tipo string
    #json.loads retorna a string passada convertida em um dicionário
    coordenadas = (json.loads(requisicao_geoplugin.text))
    #pegando a chave geoplugin_latitude do dicionário coordenadas
    latitude = coordenadas['geoplugin_latitude']
    #pegando a chave geoplugin_longitude do dicionário coordenadas
    longitude = coordenadas['geoplugin_longitude']

    #url adaptava para usar as variáveis
    url_local_api = 'http://dataservice.accuweather.com/locations/v1/cities/geoposition/' \
    + 'search?apikey=' + chave_api \
    + '&q=' + latitude + '%2C%20' + longitude + '&language=pt-br'

    requisicao_local = requests.get(url_local_api)
    #verificando o status do site (200 OK)
    if requisicao_local.status_code != 200:
        print('Não foi possível obter o código do local.')
    else:
        localizacao = (json.loads(requisicao_local.text))
        #guardando conteúdo das chaves do dicionário na variável
        #cidade, estado - país
        nome_local = localizacao['LocalizedName'] + ', ' + localizacao['AdministrativeArea']['LocalizedName'] \
        + ' - ' + localizacao['Country']['LocalizedName']
        codigo_local = localizacao['Key']
        print(f'Obtendo clima do local: {nome_local}')

        url_tempo_api = 'http://dataservice.accuweather.com/currentconditions/v1/' \
        + codigo_local +'?apikey=' + chave_api + '&language=pt-br'

        requisicao_tempo = requests.get(url_tempo_api)
        if requisicao_tempo.status_code != 200:
            print('Não foi possível obter o código do local.')
        else:
            #aqui temos um lista e um dicionário dentro
            tempo_atual = (json.loads(requisicao_tempo.text))
            #print(pprint(tempo_atual))
            clima = tempo_atual[0]['WeatherText']
            temperatura = tempo_atual[0]['Temperature']['Metric']['Value']
            print(clima)
            print(f'Temperatura: {temperatura}°C')
