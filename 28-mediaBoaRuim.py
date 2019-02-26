'''
Informe duas notas de um aluno. Se a média for maior ou igual a 6,
a média é boa. Senão, a média é ruim.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('MÉDIA ENTRE DUAS NOTAS')

while True:
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2)/2
    print('A sua média foi {:.1f}'.format(media))
    if media >= 6:
        print('Sua média foi boa. Parabéns!!!')
    else:
        print('Sua média foi ruim. Estude mais!')
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()

rodape()
