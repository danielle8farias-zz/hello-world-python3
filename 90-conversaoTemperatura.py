'''
Crie um programa que faça a conversão de temperaturas de Celsius para Farenheit.
E de Farenheit para Celsius.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('CONVERSÃO DE TEMPERATURAS')

def cf(valor):
    f = ( (valor*9) / 5 ) + 32
    print(f'A temperatura em graus Farenheit é {f:.2f}')


def fc(valor):
    c = (5 * (valor - 32) / 9)
    print(f'A temperatura em graus Celsius é {c:.2f}')


resposta = ' '
while resposta not in '12':
    print('Digite 1 para converter de Celsius para Farenheit')
    print('Digite 2 para converter de Farenheit para Celsius')
    resposta = input('Qual conversão gostaria de fazer? ').strip()[0]
if resposta == '1':
    valor = float(input('Digite a temperatura em Celsius: '))
    cf(valor)
elif resposta == '2':
    valor = float(input('Digite a temperatura em Farenheit: '))
    fc(valor)

rodape()
