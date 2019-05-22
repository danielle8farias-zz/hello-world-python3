'''
Lendo um texto html da internet
'''
import urllib.request #permite conversar com a internet
pagina = urllib.request.urlopen('http://beans.itcarlow.ie/prices.html')
texto = pagina.read().decode('utf8')
print(texto)
preco = texto[234:238]
print(f'O preço do café hoje é: {preco}')
