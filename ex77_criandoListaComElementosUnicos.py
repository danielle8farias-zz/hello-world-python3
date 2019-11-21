'''
Crie um programa onde o usuário possa digitar vários inteiros e guarde-os em
uma lista. Caso o número já tenha sido digitado, este não será adicionado.
Retorne a lista com os valores em ordem crescente.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#programa principal
cabecalho('LISTA COM VALORES ÚNICOS EM ORDEM CRESCENTE')
#inicializando a lista
valores = []
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        #.append() adiciona um novo valor ao final da lista
        valores.append(valor)
        print('Valor adicionado com sucesso!')
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
    else:
        print('Valor duplicado. Não adicionado.')
        print()
        resposta = ' '
        #laço enquanto a resposta não for S ou N
        while resposta not in 'SN':
            resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
        if resposta == 'N':
            break
# sorted() é a função que faz a ordenação da lista
print('Os valores digitados foram: {}'.format(sorted(valores)))

rodape()
