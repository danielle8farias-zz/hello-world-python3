#!/usr/bin/env python3.8

'''
Usuário informa dois valores para as notas e programa calcula e retorna a média.
Se a média for menor do que 5, retorna que o aluno foi reprovado.
Se a média for entre 5 e 7, retorna que está de recuperação.
Se maior do que 7, está aprovado.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#função que calcula a média entre duas notas
def media(nota1,nota2):
    #atribuindo resultado da operação a variável media
    media = (nota1 + nota2)/2
    return media

#função que verifica o estado do aluno; não recebe parâmetro
def estado_aluno():
    #verifica se media é menor do que 5
    if media_info < 5:
        print('Reprovado')
    #verifica se media está entre [5 e 7)
    #cinco fechado (inclui o cinco) e sete aberto (não inclui o sete)
    #faz a verificação se a expressão lógica acima for falsa
    elif media_info > 5 and media_info < 7:
        print('Recuperação')
    else:
        print('Aprovado!')
    

#programa principal
#chamada da função cabeçalho
cabecalho('MÉDIA ESCOLAR')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() captura como string o que for digitado
    #float() convertendo string para tipo flutuante
    #atribuindo valor a variável nota1
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media_info = media(nota1, nota2)
    #função print() retorna uma string formatada na tela
    print(f'A média da nota é {media_info}')
    #chamanda da função
    estado_aluno()
    #função print() vazia não retorna nada, apenas pula uma linha
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
