'''
Leia o nome completo de uma pessoa e  mostre:
O nome com todas as letras maiúsculas.
O nome com todas as letras minúsculas.
Quantas letras têm o nome (sem considerar os espaços).
Quantas letras têm o primeiro nome.
'''
nome = input('Digite seu nome completo: ').strip()
print('Seu nome em letras maiúsculas é', nome.upper())
print('Seu nome em letras minúsculas é', nome.lower())
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
