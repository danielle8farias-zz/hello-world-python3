'''
Empacotamento de funções.
'''

#empacotamento
def contador(*num):
    print(num)


contador(1, 2, 3)
contador(4,5)
contador(9, 8, 7, 6)

#o empacotamento cria tupla
def cont(*num):
    tamanho = len(num)
    print(f'Contém {tamanho} valores.')
    for v in num:
        print(f'{v}', end=' ')
    print()


cont(1, 2, 3)
cont(4,5)
cont(9, 8, 7, 6)

def somar(*num):
    s = 0
    for i in num:
        s += i
    print(f'Soma dos valores {num}: {s}')

somar(5, 2)
somar(2, 9, 4)
