#!/usr/bin/env python3.7
'''
Calcule o preço de um aluguel de um carro, sabendo que custa R$60,00
por dia e R$0,15 por quilômetro rodado.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#função que calcula o aluguel do carro
def f_preco(dias,km):
    f_preco = dias*60 + km*0.15
    return f_preco

#programa principal
cabecalho('PREÇO ALUGUEL DE CARRO')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    dias = int(input('Dias alugados: '))
    km = float(input('Quilometros rodados: '))
    preco = f_preco(dias,km)
    #:.2f limita o número de duas casas decimais
    print(f'O total a pagar foi R${preco:.2f}')
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
