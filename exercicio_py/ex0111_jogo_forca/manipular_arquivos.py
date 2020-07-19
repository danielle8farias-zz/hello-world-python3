def abrir_arquivo(nome):
    arq = open(nome, 'rt')

    lista_itens = []
    for linha in arq:
        #removendo quebra de linha dos arquivos
        item = linha.replace('\n', '')
        #criando uma lista dos dados do arquivo
        lista_itens.append(item)
    
    return lista_itens
