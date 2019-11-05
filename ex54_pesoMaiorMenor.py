'''
Leia o peso de 5 pessoas. Mostre o maior e o menor peso lido.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#função que verifica o maior e o menor peso
def f_peso():
    maior = 0
    menor = 0
    #laço de 1 até 5
    for n in range(1,6):
        peso = float(input(f'Informe o peso da {n}ª pessoa: '))
        #se for o primeiro valor o maior e o menor são iguais
        if n == 1:
            maior = peso
            menor = peso
        else:
            if peso > maior:
                maior = peso
            elif peso < menor:
                menor = peso
    print(f'O maior peso é {maior}Kg.')
    print(f'O menor peso é {menor}Kg.')

#programa principal
cabecalho('INFORMANDO O MAIOR E O MENOR ENTRE 5 PESOS')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    f_peso()
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
