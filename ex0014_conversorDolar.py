#!/usr/bin/env python3.8
'''
Faça um conversor de Real em Dolar.
'''

#adicionando minha pasta de módulos
import sys
sys.path.append('/home/danielle8farias/Exercicios-Python-3/meus_modulos')
#importando parte do código
from mensagem import cabecalho, rodape

#função que converte o Real em Dolar
def dollar(real):
    dolar = real/3.89 #em 03/06/2019
    return dolar

#programa principal
cabecalho('CONVERSOR REAL EM DOLAR')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    real = float(input('Valor em Reais: R$'))
    valor_dolar = dollar(real)
    #:.2f limita o número de duas casas decimais
    print(f'Com R${real:.2f} você pode comprar US${valor_dolar:.2f}')
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
