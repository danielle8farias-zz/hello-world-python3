'''
Leia uma string e procure pela palavra Silva nela.
'''
nome = input('Qual seu nome completo? ').strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
