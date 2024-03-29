########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Programa retorna a previsão do tempo para cinco dias de um local escolhido pelo usuário
########

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, criar_rodape, ler_resposta

import requests
import json
from time import sleep
from datetime import datetime
from urllib.parse import quote
import pprint


chave_api = 'u5eoJmS3s9PJ0X7RYCxrKWWaZm1WJhws'
mapbox_token = 'pk.eyJ1IjoiZGFuaWVsbGU4ZmFyaWFzIiwiYSI6ImNrbWlpYmQxMzBoaWgyd211cDNmbmplajkifQ.PNrsT9uiCJLsXKAVrXW7UQ'


def pesquisar_local(local):
    local_ajustado = quote(local)
    mapbox_geocode_url = 'https://api.mapbox.com/geocoding/v5/mapbox.places/' \
        + local_ajustado + '.json?access_token=' + mapbox_token

    requisicao = requests.get(mapbox_geocode_url)
    if requisicao.status_code != 200:
        print('Não foi possível obter o local')
        return None
    else:
        try:
            resposta_mapbox = (json.loads(requisicao.text))
            coordenadas = {}
            coordenadas['longitude'] = str(resposta_mapbox['features'][0]['geometry']['coordinates'][0])
            coordenadas['latitude'] = str(resposta_mapbox['features'][0]['geometry']['coordinates'][1])
            return coordenadas
        except:
            return None


def pegar_codigo_coordenadas(latitude, longitude):
    #url adaptava para usar as variáveis
    url_local_api = 'http://dataservice.accuweather.com/locations/v1/cities/geoposition/' \
    + 'search?apikey=' + chave_api \
    + '&q=' + latitude + '%2C%20' + longitude + '&language=pt-br'

    requisicao = requests.get(url_local_api)
    if requisicao.status_code != 200:
        print('Não foi possível obter o código do local.')
        return None
    else:
        try:
            localizacao = (json.loads(requisicao.text))
            info_local = {}
            #guardando conteúdo das chaves do dicionário na variável
            #cidade, estado - país
            info_local['nome_local'] = localizacao['LocalizedName'] + ', ' + localizacao['AdministrativeArea']['LocalizedName'] \
            + ' - ' + localizacao['Country']['LocalizedName']
        
            info_local['codigo_local'] = localizacao['Key']
            return info_local
        except:
            return None


def pegar_tempo_atual(codigo_local, nome_local):
    url_tempo_api = 'http://dataservice.accuweather.com/currentconditions/v1/' \
    + codigo_local +'?apikey=' + chave_api + '&language=pt-br'

    requisicao = requests.get(url_tempo_api)
    if requisicao.status_code != 200:
        print('Não foi possível obter o clima atual.')
        return None
    else:
        try:
        #aqui temos um lista e um dicionário dentro
            tempo_atual = (json.loads(requisicao.text))
            info_clima_tempo = {}
            info_clima_tempo['clima'] = tempo_atual[0]['WeatherText']
            info_clima_tempo['temperatura'] = tempo_atual[0]['Temperature']['Metric']['Value']
            info_clima_tempo['nome_local'] = nome_local
            return info_clima_tempo
        except:
            return None


def pegar_tempo(codigo_local):
    url_tempo_api = 'http://dataservice.accuweather.com/forecasts/v1/daily/5day/' \
    + codigo_local +'?apikey=' + chave_api + '&language=pt-br&metric=true'

    requisicao = requests.get(url_tempo_api)
    if requisicao.status_code != 200:
        print('Não foi possível obter a previsão do tempo')
        return None
    else:
        try:
            #aqui temos um lista e um dicionário dentro
            previsao = (json.loads(requisicao.text))
            info_clima_tempo = []
            for dia in previsao['DailyForecasts']:
                clima_dia = {}
                #pegando o timestamp
                timestamp = dia['EpochDate']
                #objeto date_time
                date_time = datetime.fromtimestamp(timestamp)
                #formatando a data
                d = date_time.strftime('%d/%m/%Y')
                clima_dia['dia'] = d
                clima_dia['tempo_dia'] = dia['Day']['IconPhrase']
                clima_dia['tempo_noite'] = dia['Night']['IconPhrase']
                clima_dia['max'] = dia['Temperature']['Maximum']['Value']
                clima_dia['min'] = dia['Temperature']['Minimum']['Value']
                info_clima_tempo.append(clima_dia)
            return info_clima_tempo
        except:
            return None


def mostrar_previsao(latitude, longitude):
    try:
        codigo_dic = pegar_codigo_coordenadas(latitude, longitude)
        clima = pegar_tempo_atual(codigo_dic['codigo_local'], codigo_dic['nome_local'])
        print('Clima em: ' + clima['nome_local'])
        print('Temperatura: ' + str(clima['temperatura']) + '°C')
        print('Tempo: ' + clima['clima'])
    except:
        print('Erro ao obter o clima atual.')

    resposta = ler_resposta('\nDeseja saber a previsão para os próximos 4 dias? [S/N] ')
    if resposta == 'S':
        print('\nClima hoje e para os próximos 4 dias: ')
        try:
            previsao = pegar_tempo(codigo_dic['codigo_local'])
            for dia in previsao:
                sleep(0.5)
                print(dia['dia'])
                print('Tempo para o dia: ' + dia['tempo_dia'])
                print('Tempo para a noite: ' + dia['tempo_noite'])
                print('Temperatura máxima: ' + str(dia['max']) + '°C')
                print('Temperatura mínima: ' + str(dia['min']) + '°C\n')
                sleep(0.5)
        except:
            print('Erro ao obter a previsão do tempo para os próximos dias.')


#main
ler_cabecalho('previsão do tempo')

print('Digite a cidade e o estado para o qual deseja ver a previsão do tempo')
local = input('[cidade, estado ]: ')
coordenadas_dic = pesquisar_local(local)
try:
    mostrar_previsao(coordenadas_dic['latitude'], coordenadas_dic['longitude'])
except:
    print('Erro. Não foi possível obter a previsão do tempo.')

criar_rodape()
