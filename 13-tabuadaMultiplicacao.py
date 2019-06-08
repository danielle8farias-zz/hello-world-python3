'''
Faça a tabuada de multiplicação de vários números, um de cada vez.
O programa para quando é dado um número negativo.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#programa principal
cabecalho('TABUADA')
print('Para encerrar digite um número negativo')
num = int(input('Digite um número para ver sua tabuada: '))
#laço fazendo o programa rodar até que o usuário decida parar
while num >= 0:
    print('-'*40)
    #laço que vai de 0 a 10
    for i in range (0,11):
        multiplicacao = num * i
        print(f'{num} * {i:2} = {multiplicacao}')
    print()
    print('Para encerrar digite um número negativo')
    num = int(input('Digite um número para ver sua tabuada: '))
rodape()
