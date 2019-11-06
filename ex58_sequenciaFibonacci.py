'''
Leia um número inteiro e mostre a sequência de Fibonacci dos n elementos lidos.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape
from mensagem import linha

def fib(n,n1,n2):
    #cont=3 porque começa do terceiro termo
    cont = 3
    while cont <= n:
        fib = n1 + n2
        n1 = n2
        n2 = fib
        cont += 1
        print(f'{fib} - ', end='')

#programa principal
cabecalho('SEQUÊNCIA FIBONACCI')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    n = int(input('Quantos termos você quer mostrar? '))
    n1 = 1
    n2 = 1
    linha()
    print(f'{n1} - {n2} - ', end='')
    fib(n,n1,n2)
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
