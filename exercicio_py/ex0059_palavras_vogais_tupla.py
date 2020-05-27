'''
Em uma tupla de palavras, identificar e mostrar as vogais em cada uma.
'''

tupla_palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso',
'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programadora', 'futuro')

for p in tupla_palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra.lower(), end=', ')
print('\n')
