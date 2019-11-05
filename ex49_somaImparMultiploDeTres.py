'''
Soma dos números ímpares múltiplos de 3 até 500.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#programa principal
cabecalho('Soma dos números ímpares múltiplos de 3 até 500')
#inicializando a soma
soma = 0
#laço que vai de 1 até 499 de 2 em 2
for n in range(1, 500, 2):
    #verifica se é divisível por 3
    if n % 3 == 0:
        #end=' ' faz com que ao final de cada número não pule a linha, mas dê um espaço em branco
        print(n, end=' ')
        #soma = soma + 1
        soma += n
# \n serve para pular a linha
print(f'\nA soma desses números é {soma}.')
rodape()
