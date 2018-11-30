'''
Faça um programa que leia uma palavra e troque as vogais por "*" (asterísco).
'''
print('-'*50)
print(f'{"TROCA VOGAIS POR ASTERÍSCO":^50}')
print('-'*50)
palavra = input('Escreva uma palavra: ').strip().lower()
i = 0
troca = ''
while i < len(palavra):
   if palavra[i] in 'aeiou':
      troca += '*'
   else:
       troca += palavra[i]
   i += 1
print(f'A nova palavra é: {troca}')
print('-'*50)
print(f'{"FIM":^50}')
print('-'*50)
