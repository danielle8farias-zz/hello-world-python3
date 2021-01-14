########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Programa retorna o tempo e temperatura da localidade do usuário
########

import requests
import json
#from pprint import pprint

chave_api = 'u5eoJmS3s9PJ0X7RYCxrKWWaZm1WJhws'

def pegar_coordenadas():
    #mandano uma requisição para o site indicado
    requisicao = requests.get('http://www.geoplugin.net/json.gp')

    #verificando o status do site (200 OK)
    if requisicao.status_code != 200:
        print('Não foi possível obter a localização.')
    else:
        #r.text é do tipo string
        #json.loads retorna a string passada convertida em um dicionário
        info_localizacao = (json.loads(requisicao.text))
        #criando novo dicionário para as coordenadas
        coordenadas = {}
        #pegando a chave geoplugin_latitude do dicionário info_localizacao
        coordenadas['latitude'] = info_localizacao['geoplugin_latitude']
        #pegando a chave geoplugin_longitude do dicionário info_localizacao
        coordenadas['longitude'] = info_localizacao['geoplugin_longitude']
        
        return coordenadas


def pegar_codigo_local(latitude, longitude):
    #url adaptava para usar as variáveis
    url_local_api = 'http://dataservice.accuweather.com/locations/v1/cities/geoposition/' \
    + 'search?apikey=' + chave_api \
    + '&q=' + latitude + '%2C%20' + longitude + '&language=pt-br'

    requisicao = requests.get(url_local_api)
    if requisicao.status_code != 200:
        print('Não foi possível obter o código do local.')
    else:
        localizacao = (json.loads(requisicao.text))
        info_local = {}
        #guardando conteúdo das chaves do dicionário na variável
        #cidade, estado - país
        info_local['nome_local'] = localizacao['LocalizedName'] + ', ' + localizacao['AdministrativeArea']['LocalizedName'] \
        + ' - ' + localizacao['Country']['LocalizedName']
        
        info_local['codigo_local'] = localizacao['Key']
        
        return info_local


def pegar_tempo_atual(codigo_local, nome_local):
    url_tempo_api = 'http://dataservice.accuweather.com/currentconditions/v1/' \
    + codigo_local +'?apikey=' + chave_api + '&language=pt-br'

    requisicao = requests.get(url_tempo_api)
    if requisicao.status_code != 200:
        print('Não foi possível obter o código do local.')
    else:
        #aqui temos um lista e um dicionário dentro
        tempo_atual = (json.loads(requisicao.text))
        info_clima_tempo = {}
        info_clima_tempo['clima'] = tempo_atual[0]['WeatherText']
        info_clima_tempo['temperatura'] = tempo_atual[0]['Temperature']['Metric']['Value']
        info_clima_tempo['nome_local'] = nome_local

        return info_clima_tempo

#main
