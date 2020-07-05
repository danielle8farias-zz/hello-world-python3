#!/usr/bin/env python3.8

'''
Usuário informa 3 números inteiros e programa retorna o maior e o menor deles.
'''

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, rodape, ler_resposta
from numeros import ler_num_int


#função para caso os 3 números sejam diferentes entre si
def num_diferentes(num1,num2,num3):
    #verificando se num1 é maior do que num2 e num3
    if (num1 > num2) and (num1 > num3):
        print(f'O maior número é {num1} ',end='')
        #verificando quem é o maior entre num2 e num3
        if num2 > num3:
            print(f'e o menor é {num3}')
        else:
            print(f'e o menor é {num2}')
    #verificando se num2 é maior do que num1 e num3
    elif (num2 > num1) and (num2 > num3):
        print(f'O maior número é {num2} ',end='')
        #verificando quem é o maior entre num1 e num3
        if num1 > num3:
            print(f'e o menor é {num3}')
        else:
            print(f'e o menor é {num1}')
    #caso o num3 seja o maior
    else: #(num3 > num1) and (num3 > num2):
        print(f'O maior número é {num3} ',end='')
        #verificando quem é o maior entre num1 e num2
        if num1 > num2:
            print(f'e o menor é {num2}')
        else:
            print(f'e o menor é {num1}')


#função para o caso em que dois números são iguais
def num_dois_iguais(num1,num2,num3):
    #verificando se num1 é igual a algum outro
    if (num1 == num2) or (num1 == num3):
        print(f'O maior número é {num1} ',end='')
        #verificando quem é o maior entre num2 e num3
        if num2 > num3:
            print(f'e o menor é {num3}')
        else:
            print(f'e o menor é {num2}')
    #verificando se num2 é igual a algum outro     
    elif (num2 == num1) or (num2 == num3) :
        print(f'O maior número é {num2} ',end='')
        #verificando quem é o maior entre num1 e num3
        if num1 > num3:
            print(f'e o menor é {num3}')
        else:
            print(f'e o menor é {num1}')
    #caso num3 seja igual a algum outro
    else: #(num3 == num1) or (num3 == num2):
        print(f'O maior número é {num3} ',end='')
        #verificando quem é o maior entre num1 e num2
        if num1 > num2:
            print(f'e o menor é {num2}')
        else:
            print(f'e o menor é {num1}')


#função que verifica os números; pré-seleção dos números
def f_maior(num1, num2, num3):
    #verifica se os 3 números são diferentes entre si
    if (num1 != num2) and (num1 != num3) and (num2 != num3):
        num_diferentes(num1,num2,num3)
    #verifica se os 3 números são iguais entre si        
    elif (num1 == num2) and ( num1 == num3) and (num2 == num3):
        print('Os valores são iguais!')
    #caso 2 números sejam iguais entre si
    else:
        num_dois_iguais(num1,num2,num3)


#programa principal
ler_cabecalho('MAIOR ENTRE TRÊS NÚMEROS')
while True:
    num1 = ler_num_int("Digite o 1º número inteiro: ")
    num2 = ler_num_int("Digite o 2º número inteiro: ")
    num3 = ler_num_int("Digite o 3º número inteiro: ")
    #chamada da função que pré-seleciona os números
    f_maior(num1, num2, num3)
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = ler_resposta('Deseja continuar? [S/N] ')
    print()
    if resposta == 'N':
        break
rodape()


'''
# teste
f_maior(1, 2, 3)
f_maior(11, 13, 12)
f_maior(22, 21, 23)
f_maior(32, 33, 31)
f_maior(43, 42, 41)
f_maior(53, 51, 52)
f_maior(63, 63, 62)
f_maior(73, 72, 73)
f_maior(82, 83, 83)
f_maior(93, 93, 93)
'''