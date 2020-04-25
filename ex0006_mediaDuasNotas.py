#!/usr/bin/env python3.8

'''
Usuário informa dois valores para as notas e programa calcula e retorna a média.
Se a média for menor do que 5, retorna que o aluno foi reprovado.
Se a média for entre 5 e 7, retorna que está de recuperação.
Se maior do que 7, está aprovado.
'''

#adicionando minha pasta de módulos
import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#função que calcula a média entre duas notas
def media(nota1,nota2):
    media = (nota1 + nota2)/2
    return media

#programa principal
cabecalho('MÉDIA ESCOLAR')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() captura o que for digitado no teclado
    #float() faz a conversão da string para tipo flutuante
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
    #inicializa a variável vazia para entrar no 2º laço
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
