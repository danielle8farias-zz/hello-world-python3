#!/usr/bin/env python3.8

'''
Usuário digita, em números, a data completa de nascimento e programa retorna essa informação formatada.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape
#importando módulo de data
from datetime import date

#criando a classe
class Nascimento:
    #método da classe sem a referência a si mesma
    @classmethod
    #método da classe captura o dia informado pelo usuário
    def dia(cls):
        '''
        captura e faz a validação do dia informado
        '''
        while True:
            #input() captura como string o que for digitado
            #int() convertendo a string recebida para tipo inteiro
            #atribuindo valor a variável dia
            dia = int(input('Digite o dia do seu nascimento: '))
            #limitando o dia de 1 a 31
            if dia > 0 and dia < 32:
                return dia
                #quebra o laço
                break
            else:
                #função print() retorna uma string
                print('Digite uma data válida!')

    @classmethod
    def mes(cls):
        '''
        captura a faz a validação do mês informado
        '''
        while True:
            mes = int(input('Digite o número do mês do seu nascimento: '))
            #limitando o mês de 1 a 12
            if mes > 0 and mes < 13:
                return mes
                break
            else:
                print('Digite uma data válida!')

    @classmethod
    def ano(cls):
        '''
        captura a faz a validação do ano informado
        '''
        while True:
            #date.today().year pega o ano indicado pelo sistema operacional
            #retirando 5 anos do ano atual
            ano_atual = date.today().year - 5
            ano = int(input('Digite o ano do seu nascimento: '))
            #limitando o ano de 1901 até o ano atual
            if ano > 1900 and ano < ano_atual:
                return ano
                break
            else:
                print('Digite uma data válida!')

#programa principal
#chamada da função cabeçalho
cabecalho('data completa do nascimento')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #chamando as funções e atribuindo os seus retornos à variáveis
    dia = Nascimento.dia()
    mes = Nascimento.mes()
    ano = Nascimento.ano()
    #função print() retorna uma string formatada na tela
    print(f'Você nasceu no dia {dia} de {mes} de {ano}.')
    # função print() vazia não retorna nada; apenas pula uma linha
    print()
    #inicializa a variável com espaço para entrar no 2º laço
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #upper: joga a string para maiúsculo
        #strip: remove os espaços no começo e no fim
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N]? ').upper().strip()[0]
    #verificando se variável reposta é igual a string N    
    if resposta == 'N':
        #quebrando o 1º laço
        break
    print()
#chamada da função rodapé    
rodape()
