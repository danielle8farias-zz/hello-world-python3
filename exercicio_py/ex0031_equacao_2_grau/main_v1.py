########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário informa os valores de A, B e C da equação do 2º grau e programa retorna se possui raízes e quais são elas.
########

#cálculos referentes à equação do segundo grau para encontrar as raízes da equação informando a, b e c.

#importando módulo de cálculo da raiz quadrada
from math import sqrt

#criando a função que vai calcular as raízes da equação
#   entradas da função são o valor de 'a', 'b' e a 'raiz de delta' previamente calculada
def calcular_raizes(a, b, raiz_delta):
    #variável 'x1' recebe o valor do cálculo à direita do sinal de igualdade
    x1 = (-b + raiz_delta)/(2 * a)
    x2 = (-b - raiz_delta)/(2 * a)
    #print() imprime uma mensagem formatada na tela
    #   f-string
    #   ':.4f' até 4 casas decimais do tipo float
    #   {dentro das chaves fica a variável}
    print(f'Raizes: {x1:.2f} e {x2:.2f}')


#criando a função que vai calcular a raiz de delta
def calcular_raiz_delta(a, b, delta):
    #chamada do módulo de raiz quadrada importada acima
    raiz_delta = sqrt(delta)
    print(f'Raiz quadrada de Delta: {raiz_delta:.2f}')
    #função chamando outra função, repassando como entrada o valor calculado no início dessa.
    calcular_raizes(a, b, raiz_delta)


#criando a função que calcula o valor de delta
def calcular_delta(a, b, c):
    #pow(base, expoente)
    delta = (pow(b, 2)) - 4 * a * c
    print(f'Delta: {delta}')

    #condicional
    #caso delta seja positivo
    if delta > 0:
        print('A equação possui duas raízes reais e diferentes.')
        #chamada da função que calcula a raiz de delta
        calcular_raiz_delta(a, b, delta)
    #else if
    #caso delta seja igual a zero
    elif delta == 0:
        print('A equação possui duas raízes reais e iguais.')
        calcular_raiz_delta(a, b, delta)
    #caso delta seja negativo
    else:
        print('A equação não possui raízes reais.')


#criando a função que vai montar a equação
def equacao_seg_grau(a, b, c):
    #montando a equação do 2º grau
    print(f'{a}X² + {b}X + {c} = 0')
    calcular_delta(a, b, c)


if __name__ == '__main__':
    #chamadas das funções
    equacao_seg_grau(5, 3, 5)
    equacao_seg_grau(1, -5, 6)
    equacao_seg_grau(9, -12, 4)
