from random import choice

def escolher_palavra(lista_palavras):
    palavra_escolhida = choice(lista_palavras)
    print(palavra_escolhida)
    return palavra_escolhida, len(palavra_escolhida)
