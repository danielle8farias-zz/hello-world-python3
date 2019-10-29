'''
Faça um programa que compare dois números.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#função que verifica o maior número
def f_maior(num1,num2):
    if num1 > num2:
        print(f'O maior número é: {num1}')
    elif num2 > num1:
        print(f'O maior número é: {num2}')
    else:
        print('Os valores são iguais.')

#programa principal
cabecalho('MAIOR ENTRE DOIS NÚMEROS')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    num1 = int (input("Digite o 1º número inteiro: "))
    num2 = int (input("Digite o 2º número inteiro: "))
    f_maior(num1,num2)
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
