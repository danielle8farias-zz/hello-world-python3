'''
Crie um caixa eletrônico. Pergunte ao usuário qual valor a ser sacado (número
inteiro) e o programa vai informar quantas cédulas de cada valor serão
entregues. O caixa possui cédulas de 50, 20, 10 e 1.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#programa principal
cabecalho('CAIXA ELETRÔNICO')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    valor = int(input('Valor inteiro a ser sacado: R$'))
    if valor >= 50:
        notas = valor//50
        valor = valor % 50
        print(f'{notas} notas de R$50')
    if valor >= 20:
        notas = valor//20
        valor = valor % 20
        print(f'{notas} notas de R$20')
    if valor >= 10:
        notas = valor//10
        valor = valor % 10
        print(f'{notas} notas de R$10')
    if valor >= 1:
        notas = valor//1
        valor = valor % 1
        print(f'{notas} notas de R$1')
    print()
    resposta = ' '
    #laço enquanto a resposta não for S ou N
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
