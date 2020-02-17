#!/usr/bin/env python3.7
'''
Em uma string verifique o número de vezes que aparece a letra A
e qual a posição da primeira letra A e da última.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#programa principal
cabecalho('verificando letra a')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #lower: joga a string para minúsculo
    #strip: remove os espaços no começo e no fim
    frase = input('Digite uma frase: ').lower().strip()
    #count() conta o número de vezes que aparece a letra indicada
    print(f'A letra A aparece {frase.count("a")} vezes.')
    #find() indica a posição do caractere
    print(f'A primeira letra A está na posição {frase.find("a")}')
    #rfind() indica a posição do caractere começando pelo final da string
    print(f'A última letra A está na posição {frase.rfind("a")}')
    print()
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #strip: remove os espaços no começo e no fim
        #upper: joga a string para maiúsculo
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        #quebrando o 1º laço
        break
rodape()
