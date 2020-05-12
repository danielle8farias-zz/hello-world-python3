#!/usr/bin/env python3.8

'''
Usuário digita um número e programa retorna o dobro, o triplo e a raiz quadrada desse.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#função que calcula o dobro do número informado
def dobro(num):
    #atribuindo resultado da multiplicação a variável dobro
    dobro = num*2
    return dobro

#função que calcula o triplo do número informado
def triplo(num):
    triplo = num*3
    return triplo

#função que calcula a raiz do número informado
def raiz(num):
    # **(1/2) elevando a meio; equivale a raiz quadrada
    raiz = num**(1/2)
    return raiz

#programa principal
#chamada da função cabeçalho
cabecalho('DOBRO, TRIPLO E RAÍZ QUADRADA')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() captura como string o que for digitado
    #float() convertendo da string para tipo flutuante
    #atribuindo valor a variável num
    num = float(input('Digite um número: '))
    #variável recebe o retorno da função chamada
    dobro_info = dobro(num)
    #função print() retorna uma string formatada na tela
    print(f'O dobro é: {dobro_info}')
    triplo_info = triplo(num)
    print(f'O triplo é: {triplo_info}')
    raiz_info = raiz(num)
    print(f'A raiz quadrada é: {raiz_info}')
    # função print() vazia não retorna nada; apenas pula uma linha
    print()
    #inicializa a variável com espaço para entrar no 2º laço
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
