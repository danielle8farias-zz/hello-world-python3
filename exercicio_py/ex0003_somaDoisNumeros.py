#!/usr/bin/env python3.8

'''
Usuário digita dois números e programa retorna a soma entre eles.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#função para somar dois números recebe dois parâmetros
def soma(x,y):
        #atribuindo soma a variável z
        z = x+y
        return z

#programa principal
#chamada da função cabeçalho
cabecalho('soma de dois números')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() captura como string o que for digitado
    #float() convertendo string para tipo flutuante
    #atribuindo valor a variável num1
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    # atribui a uma variável o retorno da função soma()
    resultado = soma(num1,num2)
    #função print() retorna uma string formatada na tela
    print(f'{num1} + {num2} = {resultado}')
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
