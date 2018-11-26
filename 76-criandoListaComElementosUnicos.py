'''
Crie um programa onde o usuário possa digitar vários inteiros e guarde-os em
uma lista. Caso o número já tenha sido digitado, este não será adicionado.
Retorne a lista com os valores em ordem crescente.
'''
print('-'*50)
print('{:^50}'.format('LISTA COM VALORES ÚNICOS EM ORDEM CRESCENTE'))
print('-'*50)
valores = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso!')
        resposta = ' '
        while resposta not in 'SN':
            resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
        if resposta == 'N':
            break
    else:
        print('Valor duplicado. Não adicionado.')
        resposta = ' '
        while resposta not in 'SN':
            resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
        if resposta == 'N':
            break
print('Os valores digitados foram: {}'.format(sorted(valores)))
print('-'*50)
print('{:^50}'.format('FIM'))
print('-'*50)
