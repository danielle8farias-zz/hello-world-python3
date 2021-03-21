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

chave_api = 'u5eoJmS3s9PJ0X7RYCxrKWWaZm1WJhws'
mapbox_token = 'pk.eyJ1IjoiZGFuaWVsbGU4ZmFyaWFzIiwiYSI6ImNrbWlpYmQxMzBoaWgyd211cDNmbmplajkifQ.PNrsT9uiCJLsXKAVrXW7UQ'

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
        codigo_dic = pegar_codigo_local(latitude, longitude)
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
coordenadas_dic = pegar_coordenadas()
try:
    mostrar_previsao(coordenadas_dic['latitude'], coordenadas_dic['longitude'])
except:
    print('Erro. Não foi possível obter a previsão do tempo.')
criar_rodape()
