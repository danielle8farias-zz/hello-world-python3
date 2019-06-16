'''
Leia 3 números e mostre o maior e o menor entre eles.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#função que verifica o maior número
def f_maior(num1, num2, num3):
    if num1 >= num2 >= num3:
        print(f'O maior número é {num1} e o menor é {num3}')
    elif num1 >= num3 >= num2:
        print(f'O maior número é {num1} e o menor é {num2}')
    elif num2 >= num1 >= num3:
        print(f'O maior número é {num2} e o menor é {num3}')
    elif num2 >= num3 >= num1:
        print(f'O maior número é {num2} e o menor é {num1}')
    elif num3 >= num1 >= num2:
        print(f'O maior número é {num3} e o menor é {num2}')
    else:
        print(f'O maior número é {num3} e o menor é {num1}')

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
