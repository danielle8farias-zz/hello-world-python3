'''
Faça um programa que peça a data de nascimento (dd/mm/aaaa) e imprima o mês por extenso.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('DATA DE NASCIMENTO (MÊS POR EXTENSO)')

while True:
    dia, mes, ano = input('Informe a sua data de nascimento (dd/mm/aaaa): ').split('/')
    mes = int(mes)-1 #porque a lista inicia em zero
    meses = ['janeiro','fevereiro','março','abril','maio','junho','julho',
            'agosto','setembro','outubro','novembro','dezembro']
    print('Você nasceu em:', end=' ')
    print(f'{dia} de {meses[mes]} de {ano}')
    print()
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
    print()

rodape()

