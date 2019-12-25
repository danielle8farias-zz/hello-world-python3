'''
Árvore de natal
'''

print('☆'.center(20))
# construindo a árvore
for i in range(1, 20, 2):
    print(('*'*i).center(20))
# tronco da árvore
for r in range(2):
    print(('||').center(19))
# base da árvore e a mensagem final
print('\====/'.center(19))
print()
print('Feliz Natal e que Jesus elimine a todos vocês!',end='\n\n')
