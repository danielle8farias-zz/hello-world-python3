'''
Leia o peso, a altura e calcule o IMC de acordo com o sexo.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#função que calcula o peso ideal masculino
def peso_masc():
    p = float(input("Digite seu peso(Kg): "))
    peso = (72.7*h)-58
    print(f'O peso ideal masc. é {peso} Kg')
    if p > peso:
        print("Você está acima do peso.")
    elif p == peso:
        print("Você está dentro do peso ideal.")
    else:
        print("Você está abaixo do peso ideal.")

#função que calcula o peso ideal feminino
def peso_fem():
    p = float(input("Digite seu peso(Kg): "))
    peso = (62.1*h)-44.7
    print(f'O peso ideal fem. é {peso} Kg')    
    if p > peso:
        print("Você está acima do peso.")
    elif p == peso:
        print("Você está dentro do peso ideal.")
    else:
        print("Você está abaixo do peso ideal.")

#programa principal
cabecalho('CÁLCULO DE IMC DE ACORDO COM O SEXO')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    h = float(input("Digite sua altura(m): "))
    sexo = ' '
    #2º laço enquanto a resposta não for F ou M
    while sexo not in 'FM':
        #upper: joga a string para maiúsculo
        #strip: remove os espaços no começo e no fim
        #[0] captura apenas o primeiro caractere
        sexo = input("Digite seu sexo: [F/M] ").upper().strip()[0]
    if sexo == "M":
        peso_masc()
    else:
        peso_fem()
    print()
    resposta = ' '
    #3º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        #quebrando o 1º laço
        break
rodape()
