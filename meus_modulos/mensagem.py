'''
funções para:
cabeçalho;
linha;
rodapé;
resposta se quer continuar.
'''

def ler_cabecalho(msg):
    '''
    recebe uma string e retorna a mesma em caixa alta com espaçamento de 50 caracteres, incluindo a string passada.
    linha pontilhada em baixo e em cima.
    '''
    print('-'*50)
    print(f'{msg.upper():^50}')
    print('-'*50)


def rodape():
    '''
    sem parâmetro
    retorna a string FIM com espaçamento de 50 caracteres, incluindo a string.
    linha pontilhada em baixo e em cima.
    '''
    print('-'*50)
    print(f'{str.upper("fim"):^50}')
    print('-'*50)


def linha():
    '''
    sem parâmetro.
    retorna sinais de = repetidos em 50 caracteres.
    '''
    print('='*50)


def ler_resposta(msg):
    '''
    Faz o programa rodar enquanto o usuário digitar S ou SIM
    '''
    while True:
        try:
            #[0] captura apenas o primeiro caractere
            #strip() remove os espaços no começo e no fim
            #upper() transforma em maiúscula
            #input() captura o que é digitado
            #atribuindo valor à variável 'resposta'
            resposta = input(msg).upper().strip()[0]
            #verifica se não está contido na string 'SN';
            #   não há conflito, pois 'resposta' captura apenas a posição inicial da string
            if resposta not in 'SN':
                #criando exceção
                raise Exception('S para sim ou N para não')
        #chama a exceção criada
        #variável 'e' retorna a mensagem da exceção
        except Exception as e:
            #print(f'') retorna uma string formatada na tela
            print(f'Resposta inválida: {e}')
            #volta para o início do laço
            continue
        #em caso de resposta vazia; 
        #   caso não haja string para pegar a posição inicial
        except IndexError:
            print(f'Resposta inválida.')
            continue
        #se o 'try' for válido
        else:
            #retorna o valor da resposta
            return resposta
