def abrir_arquivo(nome):
    arq = open(nome, 'rt')

    for linha in arq:
        #criando uma lista dos dados do arquivo
        lista_itens = linha.split(', ')
    
    return lista_itens
