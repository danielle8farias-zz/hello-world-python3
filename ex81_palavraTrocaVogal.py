'''
Faça um programa que leia uma palavra e troque as vogais por "*" (asterísco).
Exercício 77 com utilizando o "for".
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('TROCA VOGAIS POR ASTERÍSCO')

palavra = input('Escreva uma palavra: ').strip().lower()
troca = ''
for vogal in range(len(palavra)):
    if palavra[vogal] in 'aeiou':
        troca += '*'
    else:
        troca += palavra[vogal]
print(f'A nova palavra é: {troca}')

rodape()
