'''
Leia uma frase e verique se é palíndromo.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#programa principal
cabecalho('VERIFICA SE UMA FRASE É PALÍNDROMO')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #strip: remove os espaços no começo e no fim
    #lower: joga a string para minúsculo
    frase = input('Digite uma frase: ').strip().lower()
    #split() divide uma string em uma lista
    palavras = frase.split()
    #''.join() junta listas strings separada pelo caractere '' sem espaços
    junto = ''.join(palavras)
    print(junto)
    #[::-1] a lista reversa, do último item ao primeiro
    if junto == junto[::-1]:
        print('É um palíndromo!')
    else:
        print('Não é palíndromo')
    print()
    #inicializando a variável com caractere vazio para que ela permaneça no loop
    resp = ' '
    #laço enquanto a resposta não for S ou N
    while resp not in 'SN':
        #strip: remove os espaços no começo e no fim
        #[0] captura apenas o primeiro caractere
        resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        #interrompendo o 1º laço
        break
    print()
rodape()
