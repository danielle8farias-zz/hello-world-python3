try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tipo de dado inválido.')
except ZeroDivisionError:
    print('Não é possível dividor por zero.')
except KeyboardInterrupt:
    print('\nUsuário interrompeu o programa.')
else:
    print(f'Resultado: {r:.2f}')
finally:
    print('Volte sempre!')
