#!/usr/bin/env python3.8

'''
Usuário informa 3 números inteiros e programa retorna o maior e o menor deles.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#função para caso os 3 números sejam diferentes entre si
def num_diferentes(num1,num2,num3):
    #verificando se num1 é maior do que num2 e num3
    if (num1 > num2) and (num1 > num3):
        # end faz com que o print não pule para a linha seguinte
        #função print retorna uma string formatada na tela
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

#função para caso em dois números são iguais
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
        #chamada da função para números diferentes
        num_diferentes(num1,num2,num3)
    #verifica se os 3 números são iguais entre si        
    elif (num1 == num2) and ( num1 == num3) and (num2 == num3):
        print('Os valores são iguais!')
    #caso 2 números sejam iguais entre si
    else:
        #chamada da função para dois números iguais
        num_dois_iguais(num1,num2,num3)


#programa principal
#chamada da função cabeçalho
cabecalho('MAIOR ENTRE TRÊS NÚMEROS')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() recebe como string dado digitado
    #int() convertendo string para tipo inteiro
    #atribuindo valor a variável num1
    num1 = int(input("Digite o 1º número inteiro: "))
    num2 = int(input("Digite o 2º número inteiro: "))
    num3 = int(input("Digite o 3º número inteiro: "))
    #chamada da função que pré-seleciona os números
    f_maior(num1, num2, num3)
    #função print vazia não retorna nada; pula uma linha
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
    #verificando se variável reposta é igual a string N
    if resposta == 'N':
        #quebrando o 1º laço
        break
#chamada da função rodapé
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