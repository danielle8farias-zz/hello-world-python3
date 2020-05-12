#!/usr/bin/env python3.8

'''
Usuário fornece dois valores, altura e largura de uma parede, e programa retorna:
A área da parede;
A quantidade de tinta necessária para pintar a parede, sabendo-se que cada litro pinta 2m².
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#função que calcula a área; recebe dois parâmetros
def area(largura,altura):
    #atribuindo a variável o resultado da operação
    area = largura*altura
    return area

#função que calcula a quantidade de tinta
def quant_tinta(valor_area):
    quant_tinta = valor_area/2
    return quant_tinta

#programa principal
#chamada da função cabeçalho
cabecalho('CÁLCULO DA QUANTIDADE DE TINTA')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() recebe como string dado digitado
    #float() convertendo string para tipo flutuante
    #atribuindo valor a variável real
    largura = float(input('Informe a largura da parede(m): '))
    altura = float(input('Informe a altura da parede(m): '))
    #atrbuindo a variável o retorno da função
    valor_area = area(largura,altura)
    #função print retorna uma string formatada na tela
    #:.2f limita o número de duas casas decimais
    print(f'A área da parede é {valor_area:.2f}m².')
    tinta = quant_tinta(valor_area)
    #:.2f limita o número de duas casas decimais
    print(f'A quantidade de tinta necessária é {tinta:.2f} litros.')
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
