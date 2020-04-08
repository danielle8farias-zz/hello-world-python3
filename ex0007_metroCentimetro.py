#!/usr/bin/env python3.8

'''
Transforma metros em centímetros e milímetros.
'''

#adicionando minha pasta de módulos
import sys
sys.path.append('/home/danielle8farias/exercicios-python-3/meus_modulos')
#importando parte do código
from mensagem import cabecalho, rodape

#função que converte metros em centimetros e milímetros
def transforme(metros):
    cent = metros*100
    mil = metros*1000
    #retorna dois valores
    return cent, mil

#programa principal
cabecalho('CONVERSOR DE METROS PARA CM E MM')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    metros = float(input('Dê um valor em metros: '))
    # duas variáveis recebendo os valores de retorno da função
    centimetro, milimetro = transforme(metros)
    print()
    print(f'{metros} m corresponde a {centimetro} cm')
    print(f'{metros} m corresponde a {milimetro} mm')
    print()
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #upper: joga a string para maiúsculo
        #strip: remove os espaços no começo e no fim
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
         #quebrando o 1º laço
        break
rodape()
