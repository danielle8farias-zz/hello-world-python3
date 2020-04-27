#!/usr/bin/env python3.8

'''
Usuário digita um valor que representa o preço e programa retorna o novo valor com desconto de 5%.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#função que calcula o desconto de 5%
def desconto(preco):
    #atribuindo a variável o resultado da operação
    desconto = preco - (preco*0.05)
    return desconto

#programa principal
#chamada da função cabeçalho
cabecalho('DESCONTO 5%')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() recebe como string dado digitado
    #float() convertendo string para tipo flutuante
    #atribuindo valor a variável real
    preco = float(input('Digite o preço: R$'))
    #atrbuindo a variável o retorno da função
    valor_desconto = desconto(preco)
    #função print retorna uma string formatada na tela
    #:.2f limita o número de duas casas decimais
    print(f'O novo preço com desconto de 5% é R${valor_desconto:.2f}')
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
