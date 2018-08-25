'''
Informe um ângulo e calcule o valor do seno, cosseno e tangente.
'''
import math
angulo = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(angulo))
print('O seno é {:.2f}'.format(seno))
cosseno = math.cos(math.radians(angulo))
print('O cosseno é {:.2f}'.format(cosseno))
tangente = math.tan(math.radians(angulo))
print('A tangente é {:.2f}'.format(tangente))
