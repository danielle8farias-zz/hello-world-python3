'''
Leia vários números inteiros e ao final apresenta a quantidade de números
digitados e a soma entre eles.
Parar quando digitar 999.
'''
n = int(input('Digite um número [999 para parar]: '))
soma = cont = 0
while n != 999:
    soma += n
    n = int(input('Digite um número [999 para parar]: '))
    cont += 1
print('Foram digitados {} números.'.format(cont))
print('A soma é {}.'.format(soma))
