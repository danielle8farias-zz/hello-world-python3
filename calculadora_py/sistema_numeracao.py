import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho
from numeros import ler_num_int, ler_num_nat


def f_escolha(opcao, num):
    if opcao == 1:
        print(f'Em binário: {bin(num)[2:]}')
    elif opcao == 2:
        print(f'Em octal: {oct(num)[2:]}')
    elif opcao == 3:
        print(f'Em hexadecimal: {hex(num)[2:]}')
    else:
        print('Opção inválida!')



def bases():
    ler_cabecalho('BASES BINÁRIA, OCTAL E HEXADECIMAL')
    num = ler_num_int('Digite um número inteiro: ')
    print('''Escolha a base para conversão:
    [1] binário
    [2] octal
    [3] hexadecimal''')
    opcao = ler_num_nat('Sua opção: ')
    f_escolha(opcao, num)
