import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import *
from numeros import ler_num_int, ler_num_float, ler_num_nat

from ex0118_interface import menu
from ex0118_manipular_arquivo import *

from time import sleep

arquivo = 'ex0118_dados_pessoas.txt'

if not arquivo_existe(arquivo):
    criar_arquivo(arquivo)


while True:
    ler_cabecalho('sistema de cadastro')
    resposta = menu(['Listar pessoas', 'Cadastrar pessoa', 'Sair do sistema'])
    if resposta == 1:
        #listar pessoas
        ler_arquivo(arquivo)
    elif resposta == 2:
        ler_cabecalho('novo cadastro')
        nome = input('Nome: ')
        idade = ler_num_nat('Idade: ')
        cadastrar_pessoa(arquivo, nome, idade)
    elif resposta == 3:
        print('Saindo do sistema')
        sleep(0.5)
        rodape()
        sleep(0.5)
        break
    else:
        print('Erro! Digite uma opção válida.')
    sleep(1)

