'''
Contagem de números pares até 50.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#programa principal
cabecalho('CONTAGEM Nº PARES ATÉ 50')
#laço que conta a partir de 2 até 50, de 2 em 2
for i in range(2, 51, 2):
    #end=' ' faz com que ao final de cada número não pule a linha, mas dê um espaço em branco
    print(i, end=' ')
print()
rodape()
