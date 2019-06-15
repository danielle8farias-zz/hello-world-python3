'''
Verifique se o número é ímpar ou par.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#função que calcula se o número é par ou ímpar
def par_impar(num):
    if num % 2 == 1:
        print(f'O número {num} é ímpar.')
    else:
        print(f'O número {num} é par.')

#programa principal
cabecalho('VERIFICA SE É PAR OU ÍMPAR')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    num = int(input("Digite um número: "))
    par_impar(num)
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
