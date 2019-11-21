'''
Leia quatro valores pelo teclado e armazene em uma tupla. Verifique:
- quantas vezes apareceu o valor 9;
- posição do primeiro valor 3;
- quais foram os números pares.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#programa principal
cabecalho('ANÁLISE DE DADOS EM UMA TUPLA')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    num = (int(input('Digite o 1º número: ')),
            int(input('Digite o 2º número: ')),
            int(input('Digite o 3º número: ')),
            int(input('Digite o 4º número: ')))
    print(f'Os números digitados foram: {num}')
    print(f'O valor 9 apareceu {num.count(9)} vezes.')
    if 3 in num:
        print(f'O valor 3 apareceu na {num.index(3)+1}ª posição.')
    else:
        print('Não há número 3.')
    print('Os valores pares são: ',end='')
    for i in num:
        if i % 2 == 0:
            print(i, end=' - ')
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
