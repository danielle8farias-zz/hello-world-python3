#args; usado por convenção da comunidade
def numeros(*args):
    #retorna argumentos empacotados numa tupla
    return args


variavel = numeros(1, 2, 3, 4, 5)
print(variavel)
#mostrando o primeiro valor
print(variavel[0])
#mostrando o último valor
print(variavel[-1])
print(len(variavel))
#montando uma lista a partir de uma tupla
lista = list(variavel)
print(lista)

#passando a lista dentro de uma função, ela retorna como um item da tupla
print(numeros(lista))
variavel1 = numeros(lista)
#acessando apenas a lista da tupla de retorno da função
print(variavel1[0])
#valores adicionados posteriormente não serão adicionados a lista
variavel1 = numeros(lista, 10, 20, 30)
print(variavel1)

#enviando a lista desempacotada
variavel2 = numeros(*lista)
print(variavel2)
#valores adicionados posteriormente também farão parte de dupla
variavel2 = numeros(*lista, 10, 20, 30)
print(variavel2)

lista1 = [10, 20, 30, 40, 50]
#as listas serão unidas numa tupla de retorno da função
variavel3 = numeros(*lista, *lista1)
print(variavel3)

#kwargs; usado por convenção da comunidade
#   argumentos com palavras chaves; dicionário
def numeros1(*args, **kwargs):
    #retorna argumentos empacotados numa tupla
    return args, kwargs


variavel4 = numeros1(*lista, *lista1, nome='danielle', sobrenome='farias')
print(variavel4)

variavel5, variavel6 = numeros1(*lista, *lista1, nome='danielle', sobrenome='farias')
print(variavel5, variavel6)
print(variavel6['nome'])
print(variavel6['sobrenome'])
print(type(variavel6))

def numeros2(*args, **kwargs):
    #verificando se foi enviado a chave 'idade'
    idade = kwargs.get('idade')
    if idade is not None:
        print(f'idade: {idade}')

    return args, kwargs


variavel7, variavel8 = numeros2(*lista, *lista1, nome='danielle', sobrenome='farias')
print(variavel7, variavel8)

variavel9, variavel10 = numeros2(*lista, *lista1, nome='danielle', sobrenome='farias', idade=30)
print('foi enviado a chave "idade"')
print(variavel9, variavel10)

def numeros3(*args, **kwargs):
    #quando se tem certeza da chave
    idade = kwargs['idade']
    print('temos a idade')
    return args, kwargs


variavel11, variavel12 = numeros3(*lista, *lista1, nome='danielle', sobrenome='farias', idade=30)
print(variavel11, variavel12)
