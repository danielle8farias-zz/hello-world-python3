'''
Leia vários números inteiros e ao final apresente a quantidade de números
digitados e a soma entre eles.
Parar quando digitar 999.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#programa principal
cabecalho('soma de vários números')
n = int(input('Digite um número [999 para parar]: '))
#inicializando as variáveis soma e cont
soma = cont = 0
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [999 para parar]: '))
print(f'Foram digitados {cont} números.')
print(f'A soma é {soma}.')
