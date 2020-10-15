########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário informa diversos números inteiros. O programa deve retornar a média desses números, qual o menor deles e o maior.
########

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_resposta
from numeros import ler_num_nat

#inicializando a variável de resposta
#   isso é necessário para entrar no laço while
resp = ' '
#inicializando as variáveis com zero
soma = cont = maior = menor = 0
while True:
    num = ler_num_nat('Digite um número: ')
    #somando os valores digitados
    soma += num
    #contando quantos valores foram digitados
    cont += 1
    #se apenas um número foi digitado, os valores de menor e maior são iguais
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    #upper() converte a string para maiúscula
    resp = ler_resposta('Deseja continuar? [S/N] ')
    if resp == 'N':
        break
    print()

media = soma/cont
print(f'\nVocê digitou {cont} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
