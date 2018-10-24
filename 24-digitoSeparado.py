'''
Leia um número de 0 a 9999 e mostre cada um dos dígitos.
'''
print('-'*50)
print('{: ^50}'.format('DÍGITOS DE UM NÚMERO'))
print('-'*50)
num = int(input("Digite um número: "))
if 0 < num <= 9999:
    mil = num //1000
    resto_m = num -(mil*1000)
    if mil == 1:
        print(mil,'milhar')
    elif mil != 0:
        print(mil,'milhares')
    cent = resto_m//100
    resto_c = resto_m - (cent*100)
    if cent == 1:
        print(cent,"centena")
    elif cent !=0:
        print(cent,"centenas")
    deze = resto_c//10
    resto_d = resto_c - (deze*10)
    if deze == 1:
        print(deze,"dezena")
    elif deze !=0:
        print(deze,"dezenas")
    unid = resto_d//1
    if unid == 1:
        print(unid,"unidade")
    elif unid !=0:
        print(unid,"unidades")
else:
    print("Valor inválido! Escolha um número maior ou igual a 1 e menor que 10000.")
