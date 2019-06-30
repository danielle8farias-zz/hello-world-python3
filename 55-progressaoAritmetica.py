'''
Leia o 1º termo de uma PA, sua razão e calcule os 10 primeiros termos.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#função que calcula os 10 primeiros termos da P.A.
def f_pa():
    A1 =  int(input('Primeiro termo: '))
    r = int(input('Razão: '))
    cont = 1
    An = A1
    while cont <= 10:
        #end=' ' para usar espaço ao invés de quebrar a linha
        print(f'{An}', end=' ')
        #usando if e else dentro do print
        print(' - ' if cont < 10 else ' ', end=' ')
        An = An + r
        cont += 1

#programa principal
cabecalho('DEZ PRIMEIROS TERMOS DE UMA P.A.')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    f_pa()
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
