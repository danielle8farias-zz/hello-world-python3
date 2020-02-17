#!/usr/bin/env python3.7
'''
Leia um número de 0 a 9999 e mostre cada um dos dígitos.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#função que separa os algarismos
def digito(num):
    #verificando se é um número maior que zero e menor que 10000
    if 0 < num <= 9999:
        #separando a unidade de milhar
        mil = num //1000
        #resto da divisão inteira da unidade de milhar
        resto_m = num -(mil*1000)
        #separando singular e plural
        if mil == 1:
            print(mil,'milhar')
        elif mil != 0:
            print(mil,'milhares')
        #separando a centena
        cent = resto_m//100
        #resto da divisão inteira da centena
        resto_c = resto_m - (cent*100)
        #separando singular e plural
        if cent == 1:
            print(cent,"centena")
        elif cent !=0:
            print(cent,"centenas")
        #separando a dezena
        deze = resto_c//10
        #resto da divisão inteira da dezena
        resto_d = resto_c - (deze*10)
        #separando singular e plural
        if deze == 1:
            print(deze,"dezena")
        elif deze !=0:
            print(deze,"dezenas")
        #separando a unidade
        unid = resto_d//1
        #separando singular e plural
        if unid == 1:
            print(unid,"unidade")
        elif unid !=0:
            print(unid,"unidades")
    else:
        print("Valor inválido! Escolha um número maior ou igual a 1 e menor que 10000.")
    
#programa principal
cabecalho('DÍGITOS DE UM NÚMERO')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    num = int(input("Digite um número inteiro: "))
    digito(num)
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
