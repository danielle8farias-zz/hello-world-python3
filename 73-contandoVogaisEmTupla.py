'''
Crie um programa que tenha em uma tupla, várias palavras (Não usar acentos).
Retornar para cada palavra as vogais contidas.
'''
print('-'*50)
print(f'{"CONTAGEM DE VOGAIS EM UMA TUPLA":^50}')
print('-'*50)
palavras = ('aprender', 'programar', 'linguagem','python','curso','gratis',
            'estudar', 'praticar','trabalhar','mercado','programador','futuro')
for p in palavras:
    print(f'\n Na palavra {p.upper()} temos', end=' ')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')
print('-'*50)
print('{:^50}'.format('FIM'))
print('-'*50)
