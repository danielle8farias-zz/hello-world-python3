#!/usr/bin/env python3.8

'''
Usuário informa o valor de uma distância(Km) que será percorrida em uma viagem.
O cálculo do preço da preço da passagem obedece os seguintes critérios:
para viagens de até 200Km, o valor é de R$0,50/Km;
acima disso o valor é R$0,45/Km.
O programa retorna o valor da passagem.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#função que calcula o preço da passagem
def f_preco(distancia):
    #verificando se a distância é menor ou igual a 200
    if distancia <= 200:
        #atribuindo a variável preço o resultado da operação
        preco = distancia * 0.5
    else:
        preco = distancia * 0.45
    #:.2f limita o número de duas casas decimais
    #função print retorna uma string formatada na tela
    print(f'Preço da passagem R${preco:.2f}')

#programa principal
#chamada da função cabeçalho
cabecalho('PREÇO DA PASSAGEM')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() recebe como string dado digitado
    #float() convertendo string para tipo flutuante
    #atribuindo valor a variável distancia
    distancia = float(input('Qual a distância da viagem?(Km) '))
    #chamada da função
    f_preco(distancia)
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
