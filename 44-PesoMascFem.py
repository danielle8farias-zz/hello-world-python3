'''
Leia o peso, a altura e calcule o IMC de acordo com o sexo.
'''
print('-'*50)
print('{: ^50}'.format('CÁLCULO DE IMC'))
print('-'*50)
while True:
    h = float(input("Digite sua altura: (m) "))
    sexo = ' '
    while sexo not in 'FM':
            sexo = input("Digite seu sexo: [F/M] ").upper().strip()[0]
    if sexo == "M":
        peso = (72.7*h)-58
        print("O peso ideal masc. é:",peso)
        p = float(input("Digite seu peso: "))
        if p > peso:
            print("Você está acima do peso.")
        elif p == peso:
            print("Você está dentro do peso ideal.")
        else:
            print("Você está abaixo do peso ideal.")
    else:
        peso = (62.1*h)-44.7
        print("O peso ideal fem. é:",peso)
        p = float(input("Digite seu peso: "))
        if p > peso:
            print("Você está acima do peso.")
        elif p == peso:
            print("Você está dentro do peso ideal.")
        else:
            print("Você está abaixo do peso ideal.")
    print()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resposta == 'N':
        break
    print()
print('-'*50)
print('{: ^50}'.format('FIM'))
print('-'*50)
