#!/usr/bin/env python3.8

'''
Leia 3 números e mostre o maior e o menor entre eles.
'''

#adicionando minha pasta de módulos
import sys
sys.path.append('/home/danielle8farias/exercicios-python-3/meus_modulos')
#importando parte do código
from mensagem import cabecalho, rodape

def num_diferentes(num1,num2,num3):
    if (num1 > num2) and (num1 > num3):
        # end faz com que o print não pule para a linha seguinte
        print(f'O maior número é {num1} ',end='')
        if num2 > num3:
            print(f'e o menor é {num3}')
        else:
            print(f'e o menor é {num2}')
    elif (num2 > num1) and (num2 > num3):
        print(f'O maior número é {num2} ',end='')
        if num1 > num3:
            print(f'e o menor é {num3}')
        else:
            print(f'e o menor é {num1}')
    else: # (num3 > num1) and (num3 > num2):
        print(f'O maior número é {num3} ',end='')
        if num1 > num2:
            print(f'e o menor é {num2}')
        else:
            print(f'e o menor é {num1}')

def num_dois_iguais(num1,num2,num3):
    if (num1 == num2) or (num1 == num3) :
        print(f'O maior número é {num1} ',end='')
        if num2 > num3:
            print(f'e o menor é {num3}')
        else:
            print(f'e o menor é {num2}')
    elif (num2 == num1) or (num2 == num3) :
        print(f'O maior número é {num2} ',end='')
        if num1 > num3:
            print(f'e o menor é {num3}')
        else:
            print(f'e o menor é {num1}')
    else: # (num3 == num1) or (num3 == num2) :
        print(f'O maior número é {num3} ',end='')
        if num1 > num2:
            print(f'e o menor é {num2}')
        else:
            print(f'e o menor é {num1}')

#função que verifica o maior número
def f_maior(num1, num2, num3):
    if (num1 != num2) and (num1 != num3) and (num2 != num3):
        num_diferentes(num1,num2,num3)
    elif (num1 == num2) and ( num1 == num3) and (num2 == num3):
        print('Os valores são iguais!')
    else:
        num_dois_iguais(num1,num2,num3)


#programa principal
cabecalho('MAIOR ENTRE TRÊS NÚMEROS')

#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    num1 = int(input("Digite o 1º número inteiro: "))
    num2 = int(input("Digite o 2º número inteiro: "))
    num3 = int(input("Digite o 3º número inteiro: "))
    f_maior(num1, num2, num3)
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