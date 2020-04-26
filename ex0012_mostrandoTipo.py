#!/usr/bin/env python3.8

'''
Usuário digita algo e programa retorna:
o seu tipo primitivo;
se o que foi digitado foi apenas a tecla espaço;
se há número no que foi digitado;
se o que foi digitado é composto de letras;
se o que foi digitado possui letras e números;
se o que foi digitado está em letras maiúsculas ou minúsculas;
e se a primeira letra é maiúscula.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#programa principal
#chamada da função cabeçalho
cabecalho('TIPO DE DADO')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #atribuindo valor a variável a
    #input() recebe como string dado digitado
    a = input('Digite algo: ')
    #função print retorna uma string formatada na tela
    print(f'O tipo primitivo desse valor é {type(a)}')
    print(f'Só tem espaços? {a.isspace()}')
    print(f'Só tem número(s)? {a.isnumeric()}')
    print(f'Só tem letras? {a.isalpha()}')
    #letras de a-z e/ou números 0-9
    print(f'É alfanumérico? {a.isalnum()}')
    print(f'Está em maiúsculas? {a.isupper()}')
    print(f'Está em minúsculas? {a.islower()}')
    #funciona apenas para string sem números
    print(f'Está capitalizada? {a.istitle()}')
    #função print vazia não retorna nada; pula uma linha
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
    #verificando se variável reposta é igual a string N
    if resposta == 'N':
        #quebrando o 1º laço
        break
#chamada da função rodapé
rodape()
