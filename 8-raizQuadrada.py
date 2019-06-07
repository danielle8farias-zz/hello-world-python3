'''
Informe a raiz quadrada de um número inteiro.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape
from math import sqrt

#função que calcula a raiz quadrada
def raiz_quadrada(num):
    raiz = sqrt(num)
    return raiz

#programa principal
cabecalho('RAÍZ QUADRADA')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    num = int(input('digite um número inteiro: '))
    raiz = raiz_quadrada(num)
    print(f'A raiz de {num} = {raiz}')
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
