'''
Leia o 1º termo de uma PA, sua razão e calcule os 10 primeiros termos.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#função que calcula cada termo da P.A.
def prog_aritm(A1, r):
    #fórmula da progressão aritmética
    An = A1 + (10-1)*r
    #laço que vai de A1 até An+r de r em r
    for n in range(A1, An + r, r):
        print(f'{n}', end = ' - ')

#programa principal
cabecalho('DEZ PRIMEIROS TERMOS DE UMA P.A.')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    A1 =  int(input('Primeiro termo: '))
    r = int(input('Razão: '))
    prog_aritm(A1, r)
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
