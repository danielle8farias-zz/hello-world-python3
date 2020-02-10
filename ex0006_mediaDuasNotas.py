#!/usr/bin/env python3.7
'''
Digite duas notas e se a média for menor do que 5, informe que foi
reprovaddo. Se a média for entre 5 e 7, informe que está de recuperação.
Se maior do que 7, está aprovado.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#função que calcula a média entre duas notas
def media(nota1,nota2):
    media = (nota1 + nota2)/2
    return media

#programa principal
cabecalho('MÉDIA ESCOLAR')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media_info = media(nota1, nota2)
    print(f'A média da nota é {media_info}')
    if media_info < 5:
        print('Reprovado')
    elif media_info > 5 and media_info < 7:
        print('Recuperação')
    else:
        print('Aprovado!')
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
