#!/usr/bin/env python3.8

'''
Usuário informa um valor de salário do funcionário e 
programa retorna o novo valor do salário com aumento.
Se o salário for superior a R$1.250,00 o aumento deve ser de 10%,
senão o aumento é de 15%.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#função que calcula o aumento do salário
def f_salario(salario):
    #verificando se salário é menor ou igual a R$1.250,00
    if salario <= 1250:
        #atribuindo a variável novo o resultado da operação
        novo = salario + (salario * 0.15)
        #função print retorna uma string na tela
        print('Aumento de 15%')
    else:
        novo = salario + (salario * 0.10)
        print('Aumento de 10%')
    #função print retorna uma string formatada na tela
    print(f'O salário novo é R${novo:.2f}')

#programa principal
#chamada da função cabeçalho
cabecalho('AUMENTO SALARIAL 10 OU 15%')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() recebe como string dado digitado
    #float() convertendo string para tipo flutuante
    #atribuindo valor a variável salario
    salario = float(input('Salário atual do funcionário: R$'))
    #chamada da função que calcula o novo salário
    f_salario(salario)
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
