'''
Informe duas notas de um aluno. Se a média for maior ou igual a 6,
a média é boa. Senão, a média é ruim.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#função que calcula a média entre duas notas
def media(nota1,nota2):
    media = (nota1 + nota2)/2
    return media

#programa principal
cabecalho('MÉDIA ENTRE DUAS NOTAS')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media_info = media(nota1, nota2)
    #:.1 limita o número a uma casas decimal
    print(f'A sua média foi {media_info:.1f}')
    if media_info >= 6:
        print('Sua média foi boa. Parabéns!!!')
    else:
        print('Sua média foi ruim. Estude mais!')
    print()
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #strip: remove os espaços no começo e no fim
        #upper: joga a string para maiúsculo
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        #quebrando o 1º laço
        break
rodape()
