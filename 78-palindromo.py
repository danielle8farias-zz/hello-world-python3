'''
Leia uma frase e verique se é palíndromo.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('VERIFICA SE UMA FRASE É PALÍNDROMO')

while True:
    frase = input('Digite uma frase: ').strip().lower()
    palavras = frase.split() #divide uma string em uma lista
    junto = ''.join(palavras) #junta listas strings separada pelo caractere ''
    print(junto)
    if junto == junto[::-1]:
        print('É um palíndromo!')
    else:
        print('Não é palíndromo')
    print()
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
    print()
rodape()
