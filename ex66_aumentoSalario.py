'''Calcula o aumento de salário dado o valor e a porcentagem'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#programa principal
cabecalho('AUMENTO DE SALÁRIO')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    salario = float(input('Salário: R$ '))
    porcentagem = float(input('Porcentagem de aumento: '))
    aumento = salario * porcentagem/100
    salario = salario + aumento
    print(f'O aumento foi de R$ {aumento:.2f}')
    print(f'O novo salário é R$ {salario:.2f}')
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
