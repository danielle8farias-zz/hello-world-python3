#!/usr/bin/env python3.8

'''
Usuário informa nome completo de uma pessoa (nome e sobrenome) e programa retorna:
o nome com todas as letras maiúsculas; depois com todas as letras minúsculas;
quantas letras têm o nome completo, sem considerar os espaços;
e quantas letras têm o primeiro nome.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#programa principal
#chamada da função cabeçalho
cabecalho('analisando seu nome')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() recebe como string dado digitado
    #strip: remove os espaços no começo e no fim
    nome = input('Digite seu nome completo: ').strip()
    #função print retorna uma string formatada na tela    
    #upper: transforma a string para maiúsculo
    print(f'Seu nome em letras maiúsculas é: {nome.upper()}')
    #lower: transforma a string para minúsculo
    print(f'Seu nome em letras minúsculas é {nome.lower()}')
    #len conta o tamanho da string e count(' ') retira os espaços entre os nomes
    #usa-se aspas duplas dentro, pois a simples já fora usada fora
    print(f'Seu nome completo tem {len(nome) - nome.count(" ")} letras')
    #find retorna a posição do caractere indicado
    #queremos que retorne até o espaço entre o primeiro nome e o próximo
    print(f'Seu primeiro nome tem {nome.find(" ")} letras')
    #função print vazia não retorna nada; pula uma linha    
    print()
    #inicializa a variável vazia para entrar no 2º laço
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    #verificando se variável reposta é igual a string N
    if resposta == 'N':
        #quebrando o 1º laço
        break
#chamada da função rodapé
rodape()
