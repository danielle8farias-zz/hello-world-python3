'''
Usuário informa vários números inteiros. O programa deve retornar 
a média desses números, qual o menor deles e o maior.
O programa deve perguntar se o usuário quer continuar ou não a digitar mais
valores.
'''

#inicializando a variável de resposta
#   isso é necessário para entrar no laço while
resp = ' '
#inicializando as variáveis com zero
soma = cont = maior = menor = 0

while True:
    num = int(input('Digite um número inteiro: '))
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
    print()
    #upper() converte a string para maiúscula
    resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
    print()

media = soma/cont
print()
print(f'Você digitou {cont} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
print()
