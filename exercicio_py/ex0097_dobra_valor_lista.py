'''
Dobrando valores de uma lista através de uma função; com enumerate.
'''

def dobrar(lista):
    for c, v in enumerate(lista):
        lista[c] = v *2
    #não retorna nada


valores = [7, 5, 3, 9]
print(valores)
dobrar(valores)
#mesmo sem o retorno da função, a lista foi modificada
print(valores)
