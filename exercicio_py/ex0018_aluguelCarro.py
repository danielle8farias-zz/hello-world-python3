#!/usr/bin/env python3.8

'''
Usuário fornece dias e os quilômetros rodados com um carro alugado e
o programa retorna o valor a ser pago, sabendo-se que o aluguel custa
R$60,00/dia e R$0,15/Km rodado.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#função que calcula o aluguel do carro
def f_preco(dias,km):
    #atribuindo a variável o resultado da operação
    f_preco = dias*60 + km*0.15
    return f_preco

#programa principal
#chamada da função cabeçalho
cabecalho('PREÇO ALUGUEL DE CARRO')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() recebe como string dado digitado
    #int() convertendo string para tipo inteiro
    #atribuindo valor a variável dias
    dias = int(input('Dias alugados: '))
    #float() convertendo string para tipo flutuante
    km = float(input('Quilometros rodados: '))
    #atrbuindo a variável o retorno da função
    preco = f_preco(dias,km)
    #:.2f limita o número de duas casas decimais
    #função print retorna uma string formatada na tela
    print(f'O total a pagar foi R${preco:.2f}')
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
