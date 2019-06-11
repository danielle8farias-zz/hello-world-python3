'''
Leia o nome completo de uma pessoa e  mostre:
O nome com todas as letras maiúsculas.
O nome com todas as letras minúsculas.
Quantas letras têm o nome (sem considerar os espaços).
Quantas letras têm o primeiro nome.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#programa principal
cabecalho('analisando seu nome')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #strip: remove os espaços no começo e no fim
    nome = input('Digite seu nome completo: ').strip()
    #upper: joga a string para maiúsculo
    print('Seu nome em letras maiúsculas é', nome.upper())
    #lower: joga a string para minúsculo
    print('Seu nome em letras minúsculas é', nome.lower())
    #len conta o tamanho da string e count(' ') retira os espaços entre os nomes
    print(f'Seu nome tem {len(nome) - nome.count(" ")} letras')
    #find retorna a posição do caractere indicado
    print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
    print()
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        #quebrando o 1º laço
        break
rodape()
