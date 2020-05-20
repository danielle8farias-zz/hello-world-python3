'''
Usuário informa dados de string, inteiro, float e booleado. Programa retorna seus tipos primitivos.
'''

msg = 'danielle'
#type() retorna o tipo de dado
print(type(msg))
print(f'{msg} é do tipo {type(msg)}')
msg = input('Digite uma palavra ou frase: ')
print(f'{msg} é do tipo {type(msg)}')
msg = input('Digite uma palavra ou frase: ')
print(f'{msg} é do tipo {type(msg)}')
print()

num1 = '8'
print(type(num1))
print(f'{num1} é do tipo {type(num1)}')
num1 = input('Digite um número: ')
print(f'{num1} é do tipo {type(num1)}')
print()

num2 = 9
print(type(num2))
print(f'{num2} é do tipo {type(num2)}')
num2 = int(input('Digite um número inteiro: '))
print(f'{num2} é do tipo {type(num2)}')
print()

num3 = 3.141592
print(type(num3))
print(f'{num3} é do tipo {type(num3)}')
num3 = float(input('Digite um número real: '))
print(f'{num3} é do tipo {type(num3)}')
print()

verdadeiro = True
Falso = False
print(f'{type(verdadeiro)} e {type(Falso)}')
#qualquer valor em booleano recebe True
#entrada ENTER recebe False
msg = bool(input('Digite uma palavra ou frase: '))
print(f'{msg} é do tipo {type(msg)}')
num = bool(input('Digite um número inteiro: '))
print(f'{num} é do tipo {type(num)}')
num = bool(input('Digite um número real: '))
print(f'{num} é do tipo {type(num)}')
enter = bool(input('Aperte ENTER'))
print(f'{enter} é do tipo {type(enter)}')
print()
