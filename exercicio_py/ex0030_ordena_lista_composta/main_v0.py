########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: ordenação de lista composta usando expressões lambda
########

def lamb_crescente(lista: list) -> list:
    #sort() função de ordenação
    lista.sort(key=lambda lista: lista[1]) #pegando apenas o item 1 da lista, que é o preço
    return lista


def lamb_decrescente(lista: list) -> list:
    #em ordem decrescente
    lista.sort(key=lambda lista: lista[1], reverse=True)
    return lista


if __name__ == '__main__':
    #criando lista composta
    lista_precos = [['óleo de soja', 3.95], ['ketchup', 8.65], ['molho de tomate', 2.05], ['azeite', 20.50], ['macarrão', 3] ]
    print(lamb_crescente(lista_precos))
    print(lamb_decrescente(lista_precos))
