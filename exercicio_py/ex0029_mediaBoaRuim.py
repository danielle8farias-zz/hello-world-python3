#!/usr/bin/env python3.8

'''
Usuário informa duas notas de um aluno.
Se a média for maior ou igual a 6, a média é boa, senão é ruim.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#função que calcula a média entre duas notas
def media(nota1,nota2):
    #atribuindo a variável media o resultado da operação
    media = (nota1 + nota2)/2
    return media

#programa principal
#chamada da função cabeçalho
cabecalho('MÉDIA ENTRE DUAS NOTAS')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() recebe como string dado digitado
    #float() convertendo string para tipo flutuante
    #atribuindo valor a variável nota1
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    #atribuindo a variável o retorno da função
    media_info = media(nota1, nota2)
    #função print retorna uma string formatada na tela
    #:.1 limita o número a uma casas decimal
    print(f'A sua média foi {media_info:.1f}')
    #verificando se a média é maior ou igual a 6
    if media_info >= 6:
        #função print retorna uma string na tela
        print('Sua média foi boa. Parabéns!!!')
    else:
        print('Sua média foi ruim. Estude mais!')
    #função print vazia não retorna nada; pula uma linha
    print()
    #inicializa a variável vazia para entrar no 2º laço
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #strip: remove os espaços no começo e no fim
        #upper: joga a string para maiúsculo
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    #verificando se variável reposta é igual a string N
    if resposta == 'N':
        #quebrando o 1º laço
        break
#chamada da função rodapé
rodape()
