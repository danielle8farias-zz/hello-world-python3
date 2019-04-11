'''
Faça um programa que tenha uma função chamada ficha() que receba dois parâmetros opcionais: o
nome do jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador
mesmo que algum dado não tenha sido informado corretamente.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('Ficha do jogador')

def ficha(j='<desconhecido>',g=0):
    print(f'O jogador {j} fez {g} gol(s) no campeonato.')

nome = input('Nome do jogador: ')
gol = input('Números de gols: ')
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    ficha(g=gol)
else:
    ficha(nome, gol)

rodape()
