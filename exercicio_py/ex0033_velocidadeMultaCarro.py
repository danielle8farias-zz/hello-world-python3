#!/usr/bin/env python3.8

'''
Usuário informa um valor para a velocidade de um carro.
Se a velocidade ultrapassar 80km/h informando que ele foi multado.
A multa deve custar R$7,00 por cada Km acima do limite.
O programa retorna o valor da multa, se houver.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#função que verifica se há multa e faz o cálculo
def f_multa(velocidade):
    #verficando se a velocidade é maior do que 80
    if velocidade > 80:
        #função print retorna uma string na tela
        print('Você foi multado!')
        #variável multa recebe o resultado da operação
        multa = (velocidade - 80) * 7
        #função print retorna uma string formatada na tela
        #:.2f limita o número de duas casas decimais
        print(f'Sua multa foi de R${multa:.2f}')
    else:
        print('Tenha um bom dia! Dirija com segurança.')

#programa principal
#chamada da função cabeçalho
cabecalho('VERIFICAÇÃO DE VELOCIDADE')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() recebe como string dado digitado
    #float() convertendo string para tipo flutuante
    #atribuindo valor a variável velocidade
    velocidade = float(input('Qual a velocidade do carro? '))
    #chamada da função
    f_multa(velocidade)
    #função print vazia não retorna nada; pula uma linha    
    print()
    #inicializa a variável vazia para entrar no 2º laço
    resposta = ' '
    #inicializa a variável com espaço para entrar no 2º laço
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
