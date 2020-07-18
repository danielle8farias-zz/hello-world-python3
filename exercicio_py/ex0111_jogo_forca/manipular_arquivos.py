def abrir_temas():
    arq = open('temas.txt', 'rt')

    for linha in arq:
        #criando uma lista dos dados do arquivo
        tema = linha.split(', ')
    
    return tema
