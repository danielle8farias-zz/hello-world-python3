'''
Digite duas notas e se a média for menor do que 5, informe que foi
reprovaddo. Se a média for entre 5 e 7, informe que está de recuperação.
Se maior do que 7, está aprovado.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('MÉDIA ESCOLAR')

while True:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2)/2
    print('A média da nota é {}'.format(media))
    if media < 5:
        print('Reprovado')
    elif media > 5 and media < 7:
        print('Recuperação')
    else:
        print('Aprovado!')
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        break

rodape()
