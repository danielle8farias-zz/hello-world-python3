'''
Leia o sexo do usuário e só aceite os valores F ou M.
Caso esteja errado, insista até o valor correto.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#programa principal
cabecalho('Sexo do usuário')
#upper: joga a string para maiúsculo
#strip: remove os espaços no começo e no fim
#[0] captura apenas o primeiro caractere
sexo = input('Digite o sexo do usuário [F/M]: ').strip().upper()[0]
#laço que só aceita strings F ou M
while sexo not in 'FM':
    print('Entrada errada. Favor digite novamente.')
    sexo = input('Digite o sexo do usuário [F/M]: ').strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')
rodape()
