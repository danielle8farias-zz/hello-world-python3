#!/usr/bin/env python3.8

#sobre a shebang:
#   deve ser posicionada sempre no início do arquivo;
#   o interpretador é acionado ao chamar o arquivo;
#   #! é a shebang propriamente dita;
#   /usr/bin é o diretório onde ficam os arquivos binários do usuário do SO.
#   env modifica o ambiente do shell temporariamente. É ele quem vai encontrar o interpretador sem que seja necessário definir seu caminho exato.

########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição:Captura o nome da pessoa e retorna uma mensagem de boas-vindas na tela.
########

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import *

ler_cabecalho('programa de boas-vindas')

while True:
    nome = ler_palavra('Digite seu nome: ')
    print(f'Bem-vinda, {nome}!')
    resposta = ' '
    while resposta not in 'SN':
        resposta = ler_resposta('\nDeseja rodar o programa de novo? [S/N] ')
    if resposta == 'N':
        break
    criar_linha()
criar_rodape()
