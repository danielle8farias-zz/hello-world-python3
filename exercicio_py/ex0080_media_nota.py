#!/usr/bin/env python3.8

'''
Usuário informa quantas notas deseja cadastrar e informa o valor dessas notas. 
Programa calcula e retorna a média das notas.
Se a média for maior ou igual a 6, a média é boa, senão é ruim.
Com validação da entrada de dados.
'''

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, rodape, linha, ler_resposta
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
            #verificando se a nota está fora do intervalo entre 0 e 10
            if nota < 0 or nota > 10:
                raise Exception('Valores entre 0 e 10.')
        except ValueError:
            print('Digite um número.')
            continue
        except Exception as erro1:
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
    print(f'Média das notas: {media:.1f}')
    if media >= 6:
        print('Sua média foi boa. Parabéns!')
    else:
        print('Sua média foi ruim. Estude mais.')
    print()
    resposta = ler_resposta('Deseja continuar? [S/N]')
    print()
    if resposta == 'N':
        break
    else:
        linha()
        print()
rodape()
