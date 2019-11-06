'''
Leia um número e retorne seu fatorial.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#função que calcula o fatorial de um número dado
def fat(n):
    f = 1
    while n > 0:
        f *= n
        n -= 1
    return f

#programa principal
cabecalho('FATORIAL!')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    n = int(input("Digite um número: "))
    print(f'O fatorial é {fat(n)}.')
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
