'''
Faça uma função que recebe vários parâmetros com valores inteiros, analisando quantos foram passados
e qual deles é o maior.
'''
from mensagem import cabecalho
from mensagem import rodape
from mensagem import linha

cabecalho('maior número')

def maior(*n):
    cont = maior = 0
    print('Analisando os valores:')
    for valor in n:
        print(f'{valor}', end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print()
    print(f'Maior número: {maior}')
    print(f'Informados {cont} valores')


maior(2,9,4,5,7,1)
linha()
maior(4,7,0)
linha()
maior(1,2)
linha()
maior(6)
linha()
maior()

rodape()
