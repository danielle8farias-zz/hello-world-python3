'''
Crie um programa que tenha em uma tupla, várias palavras (Não usar acentos).
Retornar para cada palavra as vogais contidas.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('CONTAGEM DE VOGAIS EM UMA TUPLA')

palavras = ('aprender', 'programar', 'linguagem','python','curso','gratis',
            'estudar', 'praticar','trabalhar','mercado','programador','futuro')
for p in palavras:
    print(f'\n Na palavra {p.upper()} temos', end=' ')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')
print()
rodape()
