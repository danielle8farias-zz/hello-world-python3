#!/usr/bin/env python3.8

'''
Usuário digita valores para dois catetos de um triângulo e programa retorna a hipotenusa.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape
#importando módulo de raiz quadrada
from math import sqrt

#função que calcula a hipotenusa
def hipotenusa(b,c):
    #chamada da função sqrt que calcula a raiz quadrada
    #**2 elevado ao quadrado
    #atribuindo à variável a o retorno da função
    a = sqrt(b**2 + c**2)
    return a

#programa principal
#chamada da função cabeçalho
cabecalho('CÁLCULO DA HIPOTENUSA')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() recebe como string dado digitado
    #float() convertendo string para tipo flutuante
    #atribuindo valor a variável b
    b = float(input('Digite o primeiro cateto: '))
    c = float(input('Digite o segundo cateto: '))
    #atrbuindo a variável o retorno da função
    h = hipotenusa(b,c)
    #:.2f limita o número de duas casas decimais
    #função print retorna uma string formatada na tela
    print(f'O valor da hipotenusa é: {h:.2f}')
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
