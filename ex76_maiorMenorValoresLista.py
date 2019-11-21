'''
Leia 5 valores e guarde em uma lista. Retorne o menor e maior valores e suas
respectivas posições.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#função que captura 5 valores e verifica o maior e o menor
def digita_valores():
    #inicializando as variáveis
    menor = maior = 0
    #inicializando a lista
    valores = []
    #laço de 0 a 4 (cinco valores)
    for v in range(0,5):
        #append vai adicionando ao final da lista
        valores.append(int(input(f'Digite o {v+1}º valor inteiro: ')))
        #se for o primeiro item da lista
        if v == 0:
            #menor e maior são iguais
            maior = menor = valores[v]
        else:
            if valores[v] > maior:
                maior = valores[v]
            if valores[v] < menor:
                menor = valores[v]
    return valores, menor, maior

#programa principal
cabecalho('MAIOR E MENOR DE UMA LISTA de 5 números')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    lista_valor, valor_menor, valor_maior = digita_valores()
    print()
    print(f'Você digitou os valores: {lista_valor}')
    print(f'O maior valor é: {valor_maior} na posição', end=' ')
    #enumerate vai percorrer no laço o valor em si e o índice desse valor
    for i,v in enumerate(lista_valor):
        if v == valor_maior:
            print(f'{i}... ', end='')
    print()
    print(f'O menor valor é: {valor_menor} na posição', end=' ')
    for i,v in enumerate(lista_valor):
        if v == valor_menor:
            print(f'{i}... ', end='')
    print()
    resposta = ' '
    #laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #upper: joga a string para maiúsculo
        #strip: remove os espaços no começo e no fim
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        #quebrando o 1º laço
        break
rodape()
