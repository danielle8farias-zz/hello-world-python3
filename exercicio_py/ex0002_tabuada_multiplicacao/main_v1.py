########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário digita um número inteiro e programa retorna a tabuada de multiplicação desse.
########

num = float(input('Digite um número: '))
i = 1
#laço for:
#   repete o comando dentro dele um número determinado de vezes;
#   i foi inicializado como 1;
#   range(início, fim -1);
#   vai até 9, pois 10-1=9
for i in range(i, 10):
    print(f'{num:4} x {i} = {num*i}')
print()
