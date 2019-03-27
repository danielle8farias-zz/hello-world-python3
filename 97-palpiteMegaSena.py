'''
Faça um programa que dê palpites para o jogo da mega sena (sorteando 6 números de 1 a 60 não
repeditos). Escolha quantos jogos o usuário deseja fazer e apresente-os em ordem crescente.
'''
from mensagem import cabecalho
from mensagem import rodape
from random import randint

cabecalho('JOGA NA MEGA SENA')

#sorteando os números de 1 a 60
def num_aleatorio():
    lista_num_aleatorio = []
    i = 0
    while i < 6:
        num = randint(1,60)
        if num not in lista_num_aleatorio:
            lista_num_aleatorio.append(num)
            i += 1
    print(sorted(lista_num_aleatorio))

num_jogos = int(input('Quantos números deseja sortear? '))
for i in range(num_jogos):
    num_aleatorio()

rodape()
