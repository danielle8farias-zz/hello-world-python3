'''
Crie cinco números aleatórios e armazenar numa tupla. Mostrar os números gerados
e indicar o menor e o maior deles.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape
from random import randint

#programa principal
cabecalho('MAIOR E MENOR EM TUPLA')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #criando tuplas de 5 números aleatórios de 1 a 10
    n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
    print(f'Sorteei os valores {n}')
    print()
    print(f'O maior valor é: {max(n)}')
    print(f'O menor valor é: {min(n)}')
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
