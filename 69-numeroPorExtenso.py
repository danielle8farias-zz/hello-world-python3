'''
Crie uma tupla totalmente preenchida, com uma contagem por extenso, de zero
até vinte. O programa lê um número informado pelo usuário (0 a 20) e retorna
seu equivalente por extenso.
'''
extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito',
            'nove','dez','onze','doze','treze','catorze','quinze','dezeseis',
            'dezesete','dezoito','dezenove','vinte')
print('-'*50)
print('{: ^50}'.format('NÚMERO POR EXTENSO'))
print('-'*50)
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
print('-'*50)
print('{: ^50}'.format('FIM'))
print('-'*50)
