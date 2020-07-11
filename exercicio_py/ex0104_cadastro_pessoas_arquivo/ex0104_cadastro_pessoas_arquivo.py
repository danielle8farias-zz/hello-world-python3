import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
from mensagem import ler_cabecalho, rodape, ler_resposta
from numeros import ler_num_int, ler_num_float

from interface import menu

from time import sleep

while True:
    ler_cabecalho('sistema de cadastro')
    resposta = menu(['Listar pessoas', 'Cadastrar pessoa', 'Sair do sistema'])
    if resposta == 1:
        print('opção 1')
    elif resposta == 2:
        print('opção 2')
    elif resposta == 3:
        print('Saindo do sistema')
        sleep(0.5)
        rodape()
        sleep(0.5)
        break
    else:
        print('Erro! Digite uma opção válida.')
    sleep(1)
