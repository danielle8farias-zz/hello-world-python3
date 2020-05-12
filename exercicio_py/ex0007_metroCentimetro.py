#!/usr/bin/env python3.8

'''
Usuário informa um valor em metros e programa retorna esse em centímetros e milímetros.
'''

#importando o módulo de informações sobre o sistema
import sys
#adicionando ao final da lista de módulos o caminho para os meus módulos
sys.path.append('/home/danielle8farias/hello-world-python3/meus_modulos')
#importando módulo de cabeçalho e rodapé
from mensagem import cabecalho, rodape

#função que converte metros em centimetros e milímetros
def transforme(metros):
    #atribui o resultado da multiplicação a variável cent
    cent = metros*100
    mil = metros*1000
    #retorna dois valores
    return cent, mil

#programa principal
#chamada da função cabeçalho
cabecalho('CONVERSOR DE METROS PARA CM E MM')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #input() captura como string o que for digitado
    #float() convertendo string para tipo flutuante
    metros = float(input('Dê um valor em metros: '))
    # duas variáveis recebendo o retorno duplo da função
    centimetro, milimetro = transforme(metros)
    print()
    #função print() retorna string formatada
    print(f'{metros} m corresponde a {centimetro} cm')
    print(f'{metros} m corresponde a {milimetro} mm')
    #função print() vazia não retorna nada; pula uma linha
    print()
    #inicializa a variável com espaço para entrar no 2º laço
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #upper: joga a string para maiúsculo
        #strip: remove os espaços no começo e no fim
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    #verificando se variável reposta é igual a string N    
    if resposta == 'N':
         #quebrando o 1º laço
        break
#chamada da função rodapé
rodape()
