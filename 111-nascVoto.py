'''
Usando funções, dê o ano de nascimento do usuário e retorne se ele pode votar.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('verificando se pode votar')

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        print(f'Com {idade} anos: NÃO VOTA')
    elif 16 <= idade <18 or idade > 65:
        print(f'Com {idade} anos: VOTO OPCIONAL')
    else:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')


while True:
    ano = int(input('Informe o ano de nascimento: '))
    voto(ano)
    print()
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resp == 'N':
        break
    print()

rodape()
