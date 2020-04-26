#!/usr/bin/env python3.8

'''
Usuário informa um valor em metros e programa retorna esse em centímetros e milímetros.
'''

#adicionando minha pasta de módulos
import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
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
    #input() captura o que for digitado no teclado
    #float() faz a conversão da string para tipo flutuante
    metros = float(input('Dê um valor em metros: '))
    # duas variáveis recebendo o retorno duplo da função
    centimetro, milimetro = transforme(metros)
    print()
    print(f'{metros} m corresponde a {centimetro} cm')
    print(f'{metros} m corresponde a {milimetro} mm')
    print()
    #inicializa a variável vazia para entrar no 2º laço
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
