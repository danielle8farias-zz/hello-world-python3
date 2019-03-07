'''
Leia uma frase e verique se é palíndromo.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('palíndromo')

while True:
    frase = input('Digite uma frase: ').strip().lower()
    palavras = frase.split() #divide uma string em uma lista
    junto = ''.join(palavras) #junta listas strings separada pelo caractere ''
    inverso = ''
    for letra in range(len(junto)-1, -1, -1):
        inverso += junto[letra]
    if inverso == junto:
        print('É um palíndromo!')
        print(inverso)
    else:
        print('Não é palíndromo')
    print()
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resp == 'N':
        break
    print()

rodape()
