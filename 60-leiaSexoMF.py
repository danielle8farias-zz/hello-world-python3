'''
Leia o sexo do usuário e só aceite os valores F ou M.
Caso esteja errado, insista até o valor correto.
'''
sexo = input('Digite o sexo do usuário [F/M]: ').strip().upper()[0]
while sexo not in 'FM':
    print('Entrada errada. Favor digite novamente.')
    sexo = input('Digite o sexo do usuário [F/M]: ').strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
