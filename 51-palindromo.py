'''
Leia uma frase e verique se é palíndromo.
'''
frase = input('Digite uma frase: ').strip().lower()
palavras = frase.split() #divide uma string em uma lista
junto = ''.join(palavras) #junta listas strings separada pelo caractere ''
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('É um palíndromo!')
    print(inverso)
else:
    print('Não é palíndromo')
