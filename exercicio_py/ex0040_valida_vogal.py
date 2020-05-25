'''
Usuário informa uma vogal. Caso seja digitado consoantes, programa deve informar erro 
e pedir para que o usuário digite novamente.
'''

#[0] pega apenas o primeiro caractere da string
#strip() retira espaços em branco à direita e esquerda
#lower() converte string para minúscula
vogal = input('Digite uma vogal: ').lower().strip()[0]

#laço while
#enquanto variável 'vogal' for diferente de a, e, i, o ou u.
while vogal not in 'aeiou':
    print('Valor inválido')
    vogal = input('Digite uma vogal: ').lower().strip()[0]

print(f'Vogal "{vogal}" registrado com sucesso!')
print()
