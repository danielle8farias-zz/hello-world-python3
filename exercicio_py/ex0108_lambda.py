f1 = (lambda x, y, z: x + y + z)
#funciona semelhante a uma função
soma1 = f1(2, 5, 3)
print(soma1)


f2 = (lambda x: lambda y: x + y)
soma2 = f2(4)
print(soma2)
soma3 = soma2(3)
print(soma3)
