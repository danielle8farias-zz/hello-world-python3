'''
Dias da semana armazenadas numa tupla. Usuário escohe um número inteiro de 0 a 6 e programa retorna 
um desses dias armazenados, de acordo com a posição na tupla.
'''

dia_semana = ('domingo', 'segunda', 'terça',
'quarta', 'quinta', 'sexta', 'sábado')

while True:
    dia = int(input('Escolha um número de 0 a 6: '))
    if dia < 0 or dia > 6:
        break
    else:
        print(f'Você escolheu: {dia_semana[dia]}')
