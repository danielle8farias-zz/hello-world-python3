'''
Leia uma frase e verique se é palíndromo.
'''
print('-'*50)
print(f'{"VERIICA SE UMA FRASE É PALÍNDROMO":^50}')
print('-'*50)
frase = input('Digite uma frase: ').strip().lower()
palavras = frase.split() #divide uma string em uma lista
junto = ''.join(palavras) #junta listas strings separada pelo caractere ''
print(junto)
if junto == junto[::-1]:
    print('É um palíndromo!')
else:
    print('Não é palíndromo')
print('-'*50)
print(f'{"FIM":^50}')
print('-'*50)
