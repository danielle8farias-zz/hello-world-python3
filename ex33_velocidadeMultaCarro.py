'''
Leia a velocidade de um carro. Se ele ultrapassar 80km/h mostre
a mensagem informando que foi multado.
A multa deve custar R$7,00 por cada Km acima do limite.
'''
#importando parte do código
from mensagem import cabecalho, rodape

#função que verifica se há multa e faz o cálculo
def f_multa(velocidade):
    if velocidade > 80:
        print('Você foi multado!')
        multa = (velocidade - 80) * 7
        #:.2f limita o número de duas casas decimais
        print(f'Sua multa foi de R${multa:.2f}')
    else:
        print('Tenha um bom dia! Dirija com segurança.')

#programa principal
cabecalho('VERIFICAÇÃO DE VELOCIDADE')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    velocidade = float(input('Qual a velocidade do carro? '))
    f_multa(velocidade)
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
