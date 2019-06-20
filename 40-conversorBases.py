'''
Faça um conversor da base decimal para binária, octal e hexadecimal.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#função que escolhe a opção
def f_escolha(opcao):
    if opcao == 1:
        #[2:] corta as duas primeiras casas
        print(f'Em binário: {bin(num)[2:]}')
    elif opcao == 2:
        print(f'Em octal: {oct(num)[2:]}')
    elif opcao == 3:
        print(f'Em hexadecimal: {hex(num)[2:]}')
    else:
        print('Opção inválida!')

#programa principal
cabecalho('BASES BINÁRIA, OCTAL E HEXADECIMAL')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    num = int(input('Digite um número inteiro: '))
    print('''Escolha a base para conversão:
    [1] binário
    [2] octal
    [3] hexadecimal''')
    opcao = int(input('Sua opção: '))
    f_escolha(opcao)
    print()
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #upper: joga a string para maiúsculo
        #strip: remove os espaços no começo e no fim
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        #quebrando o 1º laço
        break
rodape()
