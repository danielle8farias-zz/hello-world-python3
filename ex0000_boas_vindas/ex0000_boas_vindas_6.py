########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição:Captura o nome da pessoa e retorna uma mensagem de boas-vindas na tela.
########

import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')

#importando todo o módulo
from mensagem import *

#chamada da função
ler_cabecalho('programa de boas-vindas')

while True:
    #chamada da função que vai fazer a validação da entrada
    nome = ler_palavra('Digite seu nome: ')
    print(f'Bem-vinda, {nome}!')
    resposta = ' '
    while resposta not in 'SN':
        #chamada da função que faz a validação da resposta
        resposta = ler_resposta('\nDeseja rodar o programa de novo? [S/N] ')
    if resposta == 'N':
        break
    #chamada da função que cria a linha pontilhada
    criar_linha()
#chamada da função que cria o rodapé de finalização do programa
criar_rodape()
