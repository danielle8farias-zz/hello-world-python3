########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição:Captura o nome da pessoa e retorna uma mensagem de boas-vindas na tela.
########


#criando uma função
#função recebe um argumento
def cabecalho(msg):
    #repete o caractere por 42 vezes
    print('-'*42)
    #upper() torna a string maiúscula
    #:^42 centralizada, ocupando 42 caracteres no mínimo
    print(f'{msg.upper():^42}')
    print('-'*42)


#chamada da função
cabecalho('programa de boas-vindas')
#atribuindo uma string a variável nome
#input() captura o que é digitado no teclado
#strip() remove espaços em branco no início e no fim da string
#capitalize() torna a primeira letra maiúscula
nome = input('Digite seu nome: ').strip().capitalize()
#print() imprime na tela mensagem formatada
print(f'Bem-vinda, {nome}!')
