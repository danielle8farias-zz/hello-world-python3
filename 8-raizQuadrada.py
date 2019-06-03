'''
Informe a raiz quadrada de um número inteiro.
'''
from mensagem import cabecalho
from mensagem import rodape
from math import sqrt

#função
def raiz_quadrada(num):
    raiz = sqrt(num)
    return raiz

#programa principal
cabecalho('RAÍZ QUADRADA')
while True:
    num = int(input('digite um número inteiro: '))
    raiz = raiz_quadrada(num)
    print(f'A raiz de {num} = {raiz}')
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        break
rodape()
