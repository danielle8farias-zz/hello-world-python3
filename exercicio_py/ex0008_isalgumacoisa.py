'''
Usuário digita dado e programa retorna se esse dado pode ser convertido para inteiro, 
se possui apenas letras, 
se possui letras e números, 
se possui somente espaços, 
se está em letras maiúsculas, 
se está em letras minúsculas, 
se possui a primeira letra maiúscula. 
'''

msg = input('Digite algo: ')
#verifica se pode ser pode ser convertido para int
print(f'Pode ser convertido para int? {msg.isnumeric()}')
print(f'Possui apenas letras? {msg.isalpha()}')
print(f'Possui letras e/ou números? {msg.isalnum()}')
print(f'É somente espaço? {msg.isspace()}')
print(f'Está em maiúsculas? {msg.isupper()}')
print(f'Está em minúsculas? {msg.islower()}')
print(f'Possui a primeira letra maiúscula? {msg.istitle()}')
