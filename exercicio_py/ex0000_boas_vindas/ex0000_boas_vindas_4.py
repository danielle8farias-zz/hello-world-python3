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

while True:
    
    #atribuindo uma string a variável nome
    #input() captura o que é digitado no teclado
    #strip() remove espaços em branco no início e no fim da string
    #capitalize() torna a primeira letra maiúscula
    nome = input('Digite seu nome: ').strip().capitalize()
    
    #print() imprime na tela mensagem formatada
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
