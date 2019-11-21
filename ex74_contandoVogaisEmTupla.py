'''
Crie um programa que tenha em uma tupla, várias palavras (Não usar acentos).
Retornar para cada palavra as vogais contidas.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#programa principal
cabecalho('CONTAGEM DE VOGAIS EM UMA TUPLA')
#tupla
palavras = ('aprender', 'programar', 'linguagem','python','curso','gratis',
            'estudar', 'praticar','trabalhar','mercado','programador','futuro')
#laço para percorrer a tupla
for p in palavras:
    #\n quebra a linha
    #upper() coloca as letras em maiúsculo
    print(f'\n Na palavra {p.upper()} temos', end=' ')
    #laço para percorrer a string
    for letra in p:
        #verifica se na string há alguma vogal
        if letra in 'aeiou':
            print(letra, end=' ')
print()
rodape()
