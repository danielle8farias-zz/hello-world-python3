#!/usr/bin/env python3.8

'''
Usuário informa o comprimento de 3 retas e programa retorna 
se é possível formar um triângulo e que tipo de triângulo.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#função que verifica e identifica o triângulo
def verifica_triangulo(lado1, lado2, lado3):
    #verificando se a soma de dois lados quaisquer é maior do que o terceiro lado
    if lado2+lado3 > lado1 and lado1+lado3 > lado2 and lado1+lado2 > lado3:
        #verificando se possui os 3 lados iguais
        if lado1 == lado2 and lado2 == lado3:
            #função print retorna uma string na tela
            print('Triângulo Equilátero: três lados iguais.')
        #verificando se possui 2 lados iguais
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print('Triângulo Isósceles: quaisquer dois lados iguais.')
        else:
            print('Triângulo Escaleno: três lados diferentes.')
    else:
        print('Esses valores não formam um triângulo.')

#programa principal
#chamada da função cabeçalho
cabecalho('VERIFICA SE É TRIÂNGULO')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() recebe como string dado digitado
    #float() convertendo string para tipo flutuante
    #atribuindo valor a variável lado1
    lado1 = float(input("Digite o 1º lado do triângulo: "))
    lado2 = float(input("Digite o 2º lado do triângulo: "))
    lado3 = float(input("Digite o 3º lado do triângulo: "))
    #chamando função que verifica triângulo
    verifica_triangulo(lado1, lado2, lado3)
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
