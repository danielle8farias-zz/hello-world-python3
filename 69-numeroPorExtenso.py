'''
Crie uma tupla totalmente preenchida, com uma contagem por extenso, de zero
até vinte. O programa lê um número informado pelo usuário (0 a 20) e retorna
seu equivalente por extenso.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#tupla
extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito',
            'nove','dez','onze','doze','treze','catorze','quinze','dezeseis',
            'dezesete','dezoito','dezenove','vinte')

#programa principal
cabecalho('NÚMERO POR EXTENSO')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    #2º laço fazendo o programa aceitar apenas os valores entre 0 e 20
    while True:
        num = int(input('Digite um número (0 a 20): '))
        if 0 <= num <= 20:
            #quebrando o 2º laço
            break
    print(f'O número escolhido foi: {extenso[num]}')
    print()
    resposta = ' '
    #laço enquanto a resposta não for S ou N
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
