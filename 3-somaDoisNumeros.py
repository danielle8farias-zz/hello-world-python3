'''
Faça a soma de dois números.
'''

from mensagem import cabecalho
from mensagem import rodape

def soma(x,y):
        z = x+y
        print(x,"+",y,"=",z)


cabecalho('soma de dois números')

while True:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    soma(num1,num2)
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        break

rodape()
