'''
Usuário tem a opção de esclher entre converter um valor de temperatura de Celsius para Farenheit ou de Farenheit para Celsius.
'''

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, rodape, ler_resposta
from numeros import ler_num_float

def opcao(n):
    while True:
        try:
            num = int(input(n))
            if num != 1 and num != 2:
                raise Exception('Digite 1 ou 2.')
        except ValueError:
            print('Digite um número inteiro.')
            continue
        except Exception as erro:
            print(f'Valor inválido: {erro}')
            continue
        else:
            return num


def cf(valor):
    f = ( (valor*9) / 5 ) + 32
    print(f'A temperatura em graus Farenheit é {f:.2f}')


def fc(valor):
    c = (5 * (valor - 32) / 9)
    print(f'A temperatura em graus Celsius é {c:.2f}')


ler_cabecalho('CONVERSÃO DE TEMPERATURAS')
while True:
    print('Digite 1 para converter de Celsius para Farenheit')
    print('Digite 2 para converter de Farenheit para Celsius')
    resposta = opcao('Qual conversão gostaria de fazer? ')
    if resposta == 1:
        valor = ler_num_float('Digite a temperatura em Celsius: ')
        cf(valor)
    elif resposta == 2:
        valor = ler_num_float('Digite a temperatura em Farenheit: ')
        fc(valor)
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = ler_resposta('Deseja continuar? [S/N] ')
    print()
    if resposta == 'N':
        break
rodape()
