########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário digita uma expressão matemática que faça uso de parenteses. O programa deverá analisar se os números de parenteses abertos correspondem aos números de parenteses fechados.
########


expre = input('Digite a expressão matemática: ')
pilha = []

for simbolo in expre:
    if simbolo == '(':
        #adicionando parenteses abertos na pilha
        pilha.append('(')
    elif simbolo == ')':
        #verifica se a pilha não está vazia
        if len(pilha) > 0:
            #remove o parentese aberto ao encontrar um fechado
            pilha.pop()
        else:
            #adicionando parenteses fechados na pilha
            pilha.append(')')
            break

#número de parenteses abertos inseridos deve ser igual ao de parenteses fechados retirados;
#   a pilha deve estar vazia ao final
if len(pilha) == 0:
    print('Expressão VÁLIDA!')
#caso a pilha não esteja vazia, significa que algum parentese não foi fechado
else:
    print('Expressão inválida.')
