'''
Leia o nome completo e retorne apenas o primeiro e o último nome.
'''
nome = input('Digite seu nome completo: ').strip()
n = nome.split()
print('Seu primeiro nome é: {}'.format(n[0]))
print('Seu último nome é: {}'.format(n[-1]))
