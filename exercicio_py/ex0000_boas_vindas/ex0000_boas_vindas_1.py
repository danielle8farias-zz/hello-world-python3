########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição:Captura o nome da pessoa e retorna uma mensagem de boas-vindas na tela.
########


#atribuindo uma string a variável nome
#input() captura o que é digitado no teclado
#strip() remove espaços em branco no início e no fim da string
#capitalize() torna a primeira letra maiúscula
nome = input('Digite seu nome: ').strip().capitalize()
#print() imprime na tela mensagem formatada
print(f'Bem-vinda, {nome}!')
