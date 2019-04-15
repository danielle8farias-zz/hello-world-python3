texto = open ('msg.txt') #esse arquivo já deve existir previamente
saida = open ('cripto.txt', 'w')
for linha in texto.readlines():
    for letra in linha:
        if letra in 'aeiou':
            saida.write('*')
        else:
            saida.write(letra)
texto.close()
saida.close()
