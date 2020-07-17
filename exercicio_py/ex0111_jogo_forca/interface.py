def escolher_tema(lista_temas):
    c = 1
    for item in lista_temas:
        print(f'{c} - {item}')
        c += 1
    print()
    opcao = int(input('Escolha um tema: '))
    return opcao
