'''
Faça um programa que peça a data de nascimento (dd/mm/aaaa) e imprima o mês por extenso.
'''
print('-'*50)
print(f'{"DATA DE NASCIMENTO (MÊS POR EXTENSO)":^50}')
print('-'*50)
dia, mes, ano = input('Informe a sua data de nascimento (dd/mm/aaaa): ').split('/')
mes = int(mes)-1 #porque a lista inicia em zero
meses = ['janeiro','fevereiro','março','abril','maio','junho','julho',
        'agosto','setembro','outubro','novembro','dezembro']
print('Você nasceu em:', end=' ')
print(f'{dia} de {meses[mes]} de {ano}')
print('-'*50)
print(f'{"FIM":^50}')
print('-'*50)
