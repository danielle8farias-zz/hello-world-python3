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
#importando módulos de auxílio
from mensagem import ler_cabecalho, rodape, linha, ler_resposta
#importando módulos de números
from numeros import ler_num_int, ler_num_float

#função que soma os elementos do vetor
def somar_vetor(num):
    #criando vetor
    lista = []
    #inicializando variável contadora
    i = 1
    #inicializando soma
    soma = 0
    #range vai até um valor a menos do parâmetro, por isso num+1
    #laço que começa em 1 e vai até num(tamanho_vetor)
    for i in range(i, num+1):
        #i assume valores de 1 a num; conforme a execução do laço
        #ler_num_float() só recebe tipos numéricos
        #atribuindo a variável os elementos do vetor
        elemento = ler_num_float(f'Digite o {i}º número: ')
        #somando os valores de cada elemento passado
        soma += elemento
        #adicionando os elementos a lista(vetor)
        lista.append(elemento)
    #retorna dois valores
    return lista, soma


#programa principal
#chamada da função que lê o cabeçalho
ler_cabecalho('soma array')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #print() retorna uma string na tela
    print('Escolhendo o tamanho do vetor...')
    #ler_num_int() só recebe tipo inteiro
    #atribui a variável 'tamanho_vetor' o retorno da função
    tamanho_vetor = ler_num_int('Digite um número inteiro: ')
    #as variáveis 'lista' e 'soma' recebem os retornos da função
    lista, soma = somar_vetor(tamanho_vetor)
    #função print vazia não retorna nada; pula uma linha
    print()
    #print(f'') retorna uma string formatada na tela
    print(f'Vetor: {lista}')
    print(f'Soma dos elementos do vetor: {soma}')
    #função print vazia não retorna nada; pula uma linha
    print()
    #chamada da função que lê a resposta
    resposta = ler_resposta('Deseja continuar? [S/N]')
    print()
    #verificando se variável 'reposta' é igual a string N
    if resposta == 'N':
        #quebrando o laço
        break
    else:
        #chamada da função linha
        linha()
        print()
#chamada da função rodapé
rodape()
