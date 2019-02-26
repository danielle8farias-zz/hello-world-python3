'''
Verifique se o número é ímpar ou par.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('VERIFICA SE É PAR OU ÍMPAR')

while True:
    num = int(input("Digite um número: "))
    if num % 2 == 1:
        print("O número",num,"é ímpar.")
    else:
        print("O número",num,"é par.")
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()

rodape()
