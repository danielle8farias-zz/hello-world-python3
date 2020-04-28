#!/usr/bin/env python3.8

'''
Usuário fornece um número inteiro que será o tamanho do array, 
em seguida insere números que serão elementos desse array.
O programa retorna a soma desses elementos.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#chamada da função cabeçalho
cabecalho('soma array')
#função print retorna uma string na tela
print('Escolhendo o tamanho do vetor:')
#input() recebe como string dado digitado
#int() convertendo string para tipo inteiro
#atribuindo valor a variável num
num = int(input('Digite um número inteiro: '))
#criando vetor
lista = []
#inicializando variável contadora
i = 1
#inicializando soma
soma = 0
#range vai até um valor a menos do parâmetro, por isso num+1
#laço que começa em 1 e vai até num
for i in range(i, num+1):
    #i assume valores de 1 a num; conforme a execução do laço
    #atribuindo a variável os elementos do vetor
    elemento = int(input(f'Digite o {i}º número: '))
    #somando os valores de cada elemento passado
    soma += elemento
    #adicionando os elementos a lista(vetor)
    lista.append(elemento)
#função print vazia não retorna nada; pula uma linha
print()
#função print retorna uma string formatada na tela
print(f'Vetor: {lista}')
print(f'Soma dos elementos do vetor: {soma}')
#chamada da função rodapé
rodape()
