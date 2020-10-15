########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário digita 5 valores inteiros. Esses valores são guardados em uma lista. A ordenação é feita no momento da inserção (sem método sort). Retorna o valor da lista ordenada.
########

num_lista = list()
for i in range(5):
    num = int(input(f'Digite o {i+1}º número: '))
    #verificando se é a primeira entrada ou
    #   se o número da entrada é maior do que o último da lista
    if i == 0 or num > num_lista[-1]:
        num_lista.append(num)
    else:
        p = 0
        #percorrendo toda a lista
        while p < len(num_lista):
            #comparando o número que será inserido com 
            #   o que já existe na lista
            if num <= num_lista[p]:
                num_lista.insert(p, num)
                break
            p += 1
print(f'Lista ordenada: {num_lista}')
