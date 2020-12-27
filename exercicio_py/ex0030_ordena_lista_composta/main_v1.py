########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: ordenação de lista composta usando expressões lambda e sorted
########

def sorted_nome(lista: list) -> list:
    #sorted não altera a  lista original
    #ordenando pelo nome, item 0 da lista
    nova_lista = sorted(lista, key=lambda item: item[0])
    return nova_lista


def sorted_itens(lista: list):
    #ordenando em ordem decrescente de valor dos itens
    nova_lista = sorted(lista, key=lambda item: item[1], reverse=True)
    return nova_lista


if __name__ == '__main__':
    #criando lista composta
    lista_precos = [['milho para pipoca', 4], ['maionese', 9.15], ['grão de bico', 3.29], ['batata', 3.49], ['goma de tapioca', 5.95] ]
    print(sorted_nome(lista_precos))
    print(sorted_itens(lista_precos))
