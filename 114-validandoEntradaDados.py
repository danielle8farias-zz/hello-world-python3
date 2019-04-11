'''
Crie um programa que tenha a função leiaInt() que vai funcionar de forma semelhante a função input,
só que fazendo a validação para aceitar apenas valor numérico.
'''

from mensagem import cabecalho
from mensagem import rodape

cabecalho('validando a entrada de dados')

def leiaInt(n):
    while True:
        num = input(n)
        if not num.isnumeric():
            print('Erro! Digite um valor válido.')
        else:
            break
    return num
    

n = leiaInt('Digite um número: ')
print(f'Número digitado: {n}')

rodape()
