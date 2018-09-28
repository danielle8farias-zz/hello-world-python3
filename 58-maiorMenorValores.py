'''
Leia vários números inteiros. No final da execução mostre a média entre eles
e qual foi o maior e o menor valor lido.
O programa deve perguntar se o usuário quer continuar ou não a digitar mais
valores.
'''
resp = 'S'
soma = cont = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um valor: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
media = soma/cont
print('Você digitou {} números e a média foi {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
