########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: O programa lê e faz uma cópia de uma imagem (arquivo).
########

# open() é a função para abrir um arquivo
# 'rb'; r de leitura e b de binário
# vamos ler o binário da imagem
# a imagem deve existir previamente
logo = open('python-logo.png', 'rb')
# gravando a leitura do arquivo binário em uma variável
data = logo.read()
# fechando o arquivo lido
logo.close()

# dando um nome diferente para a cópia que será criada
# 'wb'; w de escrita e b de binário
logo2 = open('logo-do-python.png', 'wb')
# escrevendo na variável o dado binário gravado na variável data
logo2.write(data)
# fechando o arquivo
logo2.close()
