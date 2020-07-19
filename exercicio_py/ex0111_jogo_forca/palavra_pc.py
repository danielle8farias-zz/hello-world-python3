from random import choice


def escolher_palavra(lista_palavras):
    palavra_escolhida = choice(lista_palavras)
    print(palavra_escolhida)
    return palavra_escolhida, len(palavra_escolhida)


def palavra_secreta(tamanho):
    string_oculta = '__ '*tamanho
    return string_oculta


def adivinhar_palavra(tamanho, palavra_oculta, fruta_escolhida):
    erros = 0
    forca = desenhar_forca()
    lista_chutes = []
    lista_palavra_oculta = palavra_oculta.split()
    nova_palavra1 = ' '
    print(forca[erros])
    while (erros < 6) and (fruta_escolhida != nova_palavra1):
        chute = input('\nEscolha uma letra: ') #fazer o tratamento dessa entrada de dados
        posicao = 0

        if chute not in lista_chutes:
            lista_chutes.append(chute)
            print(lista_chutes)

            if chute not in fruta_escolhida:
                erros += 1
                print(f'Você tem {erros} erros.')
                print(forca[erros])
            else:
                for letra in fruta_escolhida:
                    if chute == letra:
                        print(f'letra: {chute.upper()}, na posição: {posicao}')
                        lista_palavra_oculta[posicao] = chute.upper()
                    posicao += 1
                nova_palavra = ' '.join(lista_palavra_oculta)
                nova_palavra1 = ''.join(lista_palavra_oculta).lower()
                print(nova_palavra)
                print(nova_palavra1)

        else:
            print('Essa letra já foi escolhida! Por favor, escolha outra.')
