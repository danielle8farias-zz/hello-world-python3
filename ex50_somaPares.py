'''
Leia 6 números inteiros e mostre a soma daqueles que são pares.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#programa principal
cabecalho('SOMA DE NÚMEROS PARES')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #inicializando a soma
    soma = 0
    #laço que vai pedir ao usuário 6 números
    for i in range(1,7):
        num = int(input(f'Digite o {i}º número: '))
        #verifica se é par
        if num % 2 == 0:
            #soma = soma + num (somando os pares)
            soma += num
    print(f'Soma dos números pares = {soma}.')
    print()
    resposta = ' '
    #laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #upper: joga a string para maiúsculo
        #strip: remove os espaços no começo e no fim
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        #quebrando o 1º laço
        break
rodape()
