'''
Faça um programa que leia uma palavra e troque as vogais por "*" (asterísco).
Exercício 77 com utilizando o "for".
'''
print('-'*50)
print(f'{"TROCA VOGAIS POR ASTERÍSCO":^50}')
print('-'*50)
palavra = input('Escreva uma palavra: ').strip().lower()
troca = ''
for vogal in range(0,len(palavra)):
    if palavra[vogal] in 'aeiou':
        troca += '*'
    else:
        troca += palavra[vogal]
print(f'A nova palavra é: {troca}')
print('-'*50)
print(f'{"FIM":^50}')
print('-'*50)
