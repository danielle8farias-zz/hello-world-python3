'''
Faça um programa que leia uma palavra e troque as vogais por "*" (asterísco).
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('TROCA VOGAIS POR ASTERÍSCO')

while True:
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
   resp = ' '
   while resp not in 'SN':
      resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
   if resp == 'N':
      break

rodape()
