'''
Contando quantas vezes aparece a palavra Alice
'''

from string import punctuation #serve para retirar acentos e pontuações

arq = open ('alice.txt')
texto = arq.read() #ler todo o conteúdo do arquivo em uma única string
texto = texto.lower()
for c in punctuation:
    texto = texto.replace(c,' ')
texto = texto.split() #separando as palavras em listas

#contando as palavras com uso de dicionário
dic = {}
for p in texto:
    if p not in dic:
        dic[p] = 1
    else:
        dic[p] += 1

print(f'Alice aparece {dic["alice"]} vezes.')
arq.close()