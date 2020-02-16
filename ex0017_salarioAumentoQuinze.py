#!/usr/bin/env python3.7
'''
Leia o salário e o aumente em 15%.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#função que calcula o novo salário com aumento de 15%
def novo_salario(salario):
    novo_salario = salario + salario*0.15
    return novo_salario

#programa principal
cabecalho('SALÁRIO AUMENTO 15%')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    salario = float(input('Escreva o salário: R$'))
    valor_salario = novo_salario(salario)
    #:.2f limita o número de duas casas decimais
    print(f'O novo salário com aumento de 15% é {valor_salario:.2f}')
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
