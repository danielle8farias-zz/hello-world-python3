#usando list comprehension para dobrar os valores de uma lista

x = [1, 2, 3, 4, 5]
y = [i**2 for i in x]

print(x)
print('dobrando o valor da lista "x" com list comprehension')
print(y)

#imprimindo apenas os números ímpares de uma lista
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
z = [i for i in x if i%2==1]
print('mostrando apenas números ímpares')
print(z)
