'''
Faça um conversor da base decimal para binária, octal e hexadecimal.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('BASES BINÁRIA, OCTAL E HEXADECIMAL')

while True:
    num = int(input('Digite um número inteiro: '))
    print('''Escolha a base para conversão:
    [1] binário
    [2] octal
    [3] hexadecimal''')
    opcao = int(input('Sua opção: '))
    if opcao == 1:
        print('Em binário: {}'.format(bin(num)[2:]))
    elif opcao == 2:
        print('Em octal: {}'.format(oct(num)[2:]))
    elif opcao == 3:
        print('Em hexadecimal: {}'.format(hex(num)[2:]))
    else:
        print('Opção inválida!')
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()

rodape()
