#!/usr/bin/env python3.8

'''
Usuário informa um valor que representa o salário e programa retorna um novo valor acrescido de 15% de aumento.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#função que calcula o novo salário com aumento de 15%
def novo_salario(salario):
    #atribuindo a variável o resultado da operação
    novo_salario = salario + salario*0.15
    return novo_salario

#programa principal
#chamada da função cabeçalho
cabecalho('SALÁRIO AUMENTO 15%')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() recebe como string dado digitado
    #float() convertendo string para tipo flutuante
    #atribuindo valor a variável real
    salario = float(input('Escreva o salário: R$'))
    #atrbuindo a variável o retorno da função
    valor_salario = novo_salario(salario)
    #:.2f limita o número de duas casas decimais
    #função print retorna uma string formatada na tela
    print(f'O novo salário com aumento de 15% é {valor_salario:.2f}')
    #função print vazia não retorna nada; pula uma linha
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
