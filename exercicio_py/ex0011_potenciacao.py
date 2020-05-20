'''
Usuário informa dois números inteiros, sendo um a base e o outro o expoente. O programa retorna o cálculo da exponenciação.
'''

base = int(input('Digite um número inteiro para a base: '))
expo = int(input('Digite um número inteiro para o expoente: '))

#calculando a exponenciação
# ** executa a exponenciação
resultado = base ** expo
print(f'Resultado da exponenciação: {resultado}')
print()

#importando módulo matemático que possui o método para exponenciação
from math import pow
resultado = pow(base, expo)
print(f'Resultado: {resultado}')
print()
