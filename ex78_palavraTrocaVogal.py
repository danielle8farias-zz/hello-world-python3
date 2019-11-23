'''
Faça um programa que leia uma palavra e troque as vogais por "*" (asterísco).
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#programa principal
cabecalho('TROCA VOGAIS POR ASTERÍSCO')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #strip: remove os espaços no começo e no fim
    #lower joga a string para minúsculo
    palavra = input('Escreva uma palavra: ').strip().lower()
    i = 0
    #inicializando a variável do tipo string
    troca = ''
    while i < len(palavra):
        if palavra[i] in 'aeiou':
            #troca = troca + '*'
            troca += '*'
        else:
            #troca = troca + palavra[i]
            #recebe a letra diferente de vogal
            troca += palavra[i]
        i += 1
    print(f'A nova palavra é: {troca}')
    #inicializando a variável com caractere vazio para que ela permaneça no loop
    resp = ' '
    #laço enquanto a resposta não for S ou N
    while resp not in 'SN':
        #upper: joga a string para maiúsculo
        #[0] captura apenas o primeiro caractere
        resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
    print()
rodape()
