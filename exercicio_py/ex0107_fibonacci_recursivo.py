'''
Usuário informa um número inteiro e programa retorna o valor da sequência de Fibonacci que está na posição de número informado; usando recursividade.
'''

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, rodape
from numeros import ler_num_nat


def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


ler_cabecalho('fibonacci recursivo')
num = ler_num_nat('Digite um número: ')
#num-1 para considerar que a sequência começa em 0
valor = fibo(num-1)
print(valor)
rodape()
