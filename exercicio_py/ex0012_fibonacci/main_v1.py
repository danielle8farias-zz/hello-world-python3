########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário informa um número inteiro e programa retorna o elemento da sequência de Fibonacci correspondente ao termo.
########

'''
Usuário informa um número inteiro e programa retorna o valor da sequência de Fibonacci que está na posição de número informado; usando recursividade.
'''


def fibo(n):
    if n <= 1:
        return n
    else:
        #recursão
        return fibo(n-1) + fibo(n-2)


num = int(input('Digite um número: '))
#num-1 para considerar que na 1ª posição da sequência temos 0
valor = fibo(num-1)
print(valor)
