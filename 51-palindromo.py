'''
Leia uma frase e verique se é palíndromo.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#função que verifica se é palíndromo
def f_palindromo(frase):
    #split() divide uma string em uma lista
    palavras = frase.split()
    #junta listas strings separada pelo caractere ''(sem espaço)
    #retirando os espaços entre as palavras
    junto = ''.join(palavras)
    inverso = ''
    #laço que vai do tamanho da palavra-1 até a última string de -1 em -1
    #começa do tamanho da palavra-1 porque vai até -1
    for letra in range(len(junto)-1, -1, -1):
        #somando cada string detrás pra frente
        inverso += junto[letra]
    if inverso == junto:
        print('É um palíndromo!')
        print(inverso)
    else:
        print('Não é palíndromo')

#programa principal
cabecalho('palíndromo')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #strip: remove os espaços no começo e no fim
    #lower: joga a string para minúsculo
    frase = input('Digite uma frase: ').strip().lower()
    f_palindromo(frase)
    print()
    resposta = ' '
    #laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #upper: joga a string para maiúsculo
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        #quebrando o 1º laço
        break
rodape()
