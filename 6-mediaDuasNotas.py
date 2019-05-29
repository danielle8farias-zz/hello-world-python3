'''
Digite duas notas e se a média for menor do que 5, informe que foi
reprovaddo. Se a média for entre 5 e 7, informe que está de recuperação.
Se maior do que 7, está aprovado.
'''
from mensagem import cabecalho
from mensagem import rodape

#função
def media(nota1,nota2):
    media = (nota1 + nota2)/2
    return media


#programa principal
cabecalho('MÉDIA ESCOLAR')
while True:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media_info = media(nota1, nota2)
    print(f'A média da nota é {media_info}')
    if media_info < 5:
        print('Reprovado')
    elif media_info > 5 and media_info < 7:
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
