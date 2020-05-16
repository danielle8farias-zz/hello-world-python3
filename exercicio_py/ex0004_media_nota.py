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

def calcular_media(lista):
    tamanho = len(lista)
    soma = 0
    for i in range(tamanho):
        soma += lista[i]
    media = soma / tamanho
    return media    


def lancar_notas(n):
    while True:
        try:
            nota = float(input(n))
            if nota < 0 or nota > 10:
                raise Exception('Valores entre 0 e 10.')
        except ValueError as erro:
            #print() retorna uma string na tela
            print('Digite um número.')
            continue
        except Exception as erro1:
            #print(f'') retorna uma string formatada na tela
            print(f'Valor inválido: {erro1}')
            continue
        else:
            return nota


#programa principal
ler_cabecalho('média das notas')
while True:
    total_notas = ler_num_int('Quantas notas deseja informar? ')
    lista_notas = []
    i = 1
    for i in range (i, total_notas+1):
        nota = lancar_notas(f'{i}ª nota: ')
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
