'''
Leia o 1º termo de uma PA, sua razão e calcule os 10 primeiros termos.
Pergunta se o usuário quer mostrar mais termos.
Quando escolhido 0 termos o programa encerra.
'''
print('='*25)
print('TERMOS DE UMA PA')
print('='*25)
A1 =  int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 1
An = A1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} - '.format(An), end='')
        An = An + r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')
print('Foram mostrados {} termos.'.format(total))
