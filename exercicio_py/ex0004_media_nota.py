#!/usr/bin/env python3.8

'''
Usuário informa quantas notas deseja cadastrar e informa o valor dessas notas. 
Programa calcula e retorna a média das notas.
Se a média for maior ou igual a 6, a média é boa, senão é ruim.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulos de auxílio
from mensagem import ler_cabecalho, rodape, linha, ler_resposta
#importando módulos de números
from numeros import ler_num_int

#função que calcula a média dos elementos de uma lista
def calcular_media(lista):
    #atribui a variável 'tamanho' o tamanho da lista
    tamanho = len(lista)
    #inicializando variável
    soma = 0
    #laço 
    #   de 0 até o final do tamanho da lista
    for i in range(tamanho):
        #soma = soma + lista[i]
        #   soma cada elemento da lista
        soma += lista[i]
    media = soma / tamanho
    #retorno da função
    return media    


#função que verifica a validade dos valores das notas
def lancar_notas(n):
    #laço
    while True:
        try:
            #input() captura como string o que for digitado
            #float() convertendo a string recebida para tipo flutuante
            #atribuindo valor à variável 'nota'
            nota = float(input(n))
            #verificando se a nota está fora do intervalo entre 0 e 10
            if nota < 0 or nota > 10:
                #criando exceção
                raise Exception('Valores entre 0 e 10.')
        #caso seja digitado espaços ou ENTER
        #variável 'erro' retorna a mensagem da exceção
        except ValueError as erro:
            #print() retorna uma string na tela
            print('Digite um número.')
            #volta para o início do laço
            continue
        #chama a exceção criada
        except Exception as erro1:
            #print(f'') retorna uma string formatada na tela
            print(f'Valor inválido: {erro1}')
            continue
        #se o 'try' for válido        
        else:
            return nota


#programa principal
#chamada da função que lê o cabeçalho
ler_cabecalho('média das notas')
while True:
    #chamada da função que lê um número inteiro
    #atribui a variável 'total_notas' o retorno da função
    total_notas = ler_num_int('Quantas notas deseja informar? ')
    #criando lista
    lista_notas = []
    #inicializando contador
    i = 1
    #laço 
    #   de 1 a número total de notas + 1
    #   necessário somar a variável final do laço, pois inicializou em 1 ao invés de 0
    for i in range (i, total_notas+1):
        nota = lancar_notas(f'{i}ª nota: ')
        #adicionando um item ao final da lista
        lista_notas.append(nota)
    media = calcular_media(lista_notas)
    #:.1 limita o número a uma casas decimal
    print(f'Média das notas: {media:.1f}')
    #verificando se a média é maior ou igual a 6
    if media >= 6:
        print('Sua média foi boa. Parabéns!')
    else:
        print('Sua média foi ruim. Estude mais.')
    # função print() vazia não retorna nada; apenas pula uma linha    
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
