########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição:Captura o nome da pessoa e retorna uma mensagem de boas-vindas na tela.
########


#importando módulo criando em outro diretório:
#   módulo sys fornece acesso a algumas variáveis usadas ou mantidas pelo interpretador;
#   sys.path contém uma lista de strings que determina os caminhos de busca de módulos conhecidos pelo interpretador;
#   append() para adicionar ao final da lista o argumento passado;
#   dentro dos parênteses informe o caminho absoluto do diretório onde estão os seus módulos criados
import sys
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')

#chamando a função do módulo importado acima
from mensagem import ler_cabecalho


#chamada da função
ler_cabecalho('programa de boas-vindas')


#definindo a função
def ler_nome(msg):
    '''
    Função que faz a validação do dado de entrada.
    Aceita apenas caracteres formados por letras.
    '''
    #tentativa de recebimento do dado
    try:
        nome = input(msg).strip()
        #separando a string onde houver espaços e armazenando cada em uma lista
        lista_nome = nome.split()
        #''. separador da nova string; no caso não haverá um caractere separador
        #join() junta uma lista de string em uma única string; unida pelo separador acima
        nome = ''.join(lista_nome)
        #condicional:
        #   se nome não for apenas formado por letras
        if not nome.isalpha():
            #criando a exceção
            raise Exception('Digite apenas letras.')
    except Exception as erro:
        print(f'Valor inválido: {erro}')
        #retorna o zero
        return 0
    #se o 'try' for válido
    else:
        #retorna o valor da variável nome
        return nome.upper()


while True:
    #chamada da função
    nome = ler_nome('Digite seu nome: ')
    print(f'Bem-vinda, {nome}!')

    #variável recebe espaço
    resposta = ' '
    #laço while:
    #   enquando o valor de resposta for diferente de S ou N
    while resposta not in 'SN':
        #\n quebra de linha
        #upper() torna as letras maiúsculas
        #[0] captura apenas o primeiro caractere da string
        resposta = input('\nDeseja rodar o programa de novo? [S/N] ').upper().strip()[0]
    #condicional:
    #   se a resposta for igual a N
    if resposta == 'N':
        #quebra do laço while True
        break
