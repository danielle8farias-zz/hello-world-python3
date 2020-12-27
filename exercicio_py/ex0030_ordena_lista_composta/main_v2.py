########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: ordenação de lista composta usando método sort
########

def ordenar(lista: list) -> list:
    return lista[1]


def ordenar_preco_crescente(lista: list) -> list:
    lista_precos.sort(key=ordenar)
    return lista_precos


def ordenar_preco_decrescente(lista: list) -> list:
    lista_precos.sort(key=ordenar, reverse=True)
    return lista_precos


if __name__ == '__main__':
    lista_precos = [['lápis', 1.5], ['caneta', 2], ['caderno', 25.9], ['borracha', 1.2], ['estojo', 14.85] ]
    print(ordenar_preco_crescente(lista_precos))
    print(ordenar_preco_decrescente(lista_precos))
