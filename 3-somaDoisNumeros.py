'''
Faça a soma de dois números.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#função para somar dois números
def soma(x,y):
        z = x+y
        print(x,"+",y,"=",z)

#programa principal
cabecalho('soma de dois números')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    soma(num1,num2)
    print()
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #upper: joga a string para maiúsculo
        #strip: remove os espaços no começo e no fim
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        #quebrando o 1º laço
        break
rodape()
