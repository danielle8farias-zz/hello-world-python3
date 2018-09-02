'''
Leia o peso, a altura e calcule o IMC de acordo com o sexo.

'''
h = float(input("Digite sua altura (m): "))
print("Digite seu sexo:")
sexo = input("F para feminino e M para masculino. ")

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
