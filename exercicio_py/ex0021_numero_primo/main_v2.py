#!/usr/bin/env python3.8

########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário digita um número natural inteiro e programa verifica se esse é número primo.
########

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import *
from numeros import ler_num_nat

def verificar_primo(n):
    raiz = int(n ** (0.5))
    #raiz+1 para incluir a própria raiz; pois range tem intervalo aberto
    for divisor in range(2, raiz+1):
        if n % divisor == 0:
            return False
    return True

ler_cabecalho('verifica se é primo')
while True:
    num = ler_num_nat("Digite um número inteiro: ")
    resultado = verificar_primo(num)
    if resultado:
        print('É PRIMO!\n')
    else:
        print("não é primo\n")
    resposta = ' '
    while resposta not in 'SN':
        resposta = ler_resposta('Deseja continuar? [S/N] ')
    if resposta == 'N':
        break
    criar_linha()
criar_rodape()

####    EXPLICAÇÃO DO USO DA RAIZ   ####
# O menor divisor diferente de 1 é o número 2.
# Decompondo um número qualquer em dois fatores, sendo um deles o número 2, temos:
# N = 2 * M
# 'N' é o nosso número qualquer e 'M' a sua metade. Logo,
# M = N / 2
# Isso significa que, para divisões inteiras, o divisor não pode ser maior do que a metade do número e menor do que ele mesmo.
#
# Exemplo:
# para N = 10, temos M = 5.
# 10 = 2 * 5
# 5 = 10 / 2
# Então, o divisor de 10 não pode ser 6, 7, 8 ou 9.
# Os divisores de 10 são: 1, 2, 5 e 10.
# 
# Outro exemplo:
# para N = 45, temos M = 22,5.
# 45 = 2 * 22,5
# 22,5 = 45 / 2
# Então, o divisor de 45 não pode ser 23, 24, ... ou 44.
# Os divisores de 45 são: 1, 3, 5, 9, 15 e 45.
#
# então o range do laço for ao invés de ser:
# range(2, n)
# poderia ser:
# range(2, n//2+1)
# fazendo com que o final seja a metade, porém o valor inteiro + 1, porque o intervalo do range é aberto (isso é, vai até o valor - 1) e queremos incluir essa metade.
# 
#
### AGORA VEM A MALDITA INDUÇÃO! >_<
#
# Supondo que esse mesmo número N seja decomposto em dois fatores (X e Y),
# N = X * Y
# então 
# X = N / Y
# vamos supor que o valor de Y seja maior do que a raiz quadrada de N.
# Y > sqrt(N)
# Comparando N / Y com N /sqrt(N), temos:
# N / Y < N/sqrt(N)
# lembrando que Y > sqrt(N), ou seja o valor de N dividido por Y será um número menor porque Y é maior.
# 
# Exemplo: 10/5 < 10/2 porque 5 > 2
# 
# Fazendo a racionalização do denominador:
# N/sqrt(N)
#   N*sqrt(N) / sqrt(N)*sqrt(N)
#   N*sqrt(N) / (sqrt(N))^2     raiz quadrada de n ao quadrado
#   N*sqrt(N) / N               'cortando' a raiz com o expoente
#   sqrt(N)                     'cortando' N do numerador com o denominador
#
# então temos que 
# N / Y < sqrt(N)
# sabendo que X = N / Y
# X < sqrt(N)
#
# então, se podemos dividir o N por um número Y que é maior do que a sua raiz quadrada de N (como deduzimos acima) é porque também podemos dividir esse número N por um outro número X que é menor do que a sua raiz quadrada.
# Como para encontrar um número que não é primo só precisamos encontrar algum divisor que seja diferente de 1 e do próprio N, então só precisamos testar se existe esse X menor do que a sua raiz quadrada.
#
# por isso o range de
# range(2, n//2+1)
# pode ser 
# range(2, sqrt(n)+1)
# porque o intervalo do range é aberto (isso é, vai até o valor - 1) e queremos incluir a raiz.
# 
##############
