'''
Em uma string verifique o número de vezes que aparece a letra A
e qual a posição da primeira letra A e da última.
'''
frase = input('Digite uma frase: ').lower().strip()
print('A letra A aparece {} vezes.'.format(frase.count('a')))
print('A primeira letra A está na posição {}'.format(frase.find('a')))
print('A última letra A está na posição {}'.format(frase.rfind('a')))
