'''
Crie uma tupla totalmente preenchida, com uma contagem por extenso, de zero
até vinte. O programa lê um número informado pelo usuário (0 a 20) e retorna
seu equivalente por extenso.
'''
from mensagem import cabecalho
from mensagem import rodape

extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito',
            'nove','dez','onze','doze','treze','catorze','quinze','dezeseis',
            'dezesete','dezoito','dezenove','vinte')

cabecalho('NÚMERO POR EXTENSO')

while True:
        while True:
            num = int(input('Digite um número (0 a 20): '))
            if 0 <= num <= 20:
                break
        print('O número escolhido foi: {}'.format(extenso[num]))
        print()
        resposta = ' '
        while resposta not in 'SN':
            resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
        if resposta == 'N':
            break
        print()

rodape()
