'''
Digite duas notas e se a média for menor do que 5, informe que foi
reprovaddo. Se a média for entre 5 e 7, informe que está de recuperação.
Se maior do que 7, está aprovado.
'''
print('-'*50)
print('{: ^50}'.format('MÉDIA ESCOLAR'))
print('-'*50)
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))

media = (nota1+nota2)/2

print('A média da nota é {}'.format(media))

if media < 5:
    print('Reprovado')
elif media > 5 and media < 7:
    print('Recuperação')
else:
    print('Aprovado!')
