from urllib.request import urlopen
from webbrowser import open

try:
    site = urlopen('http://www.pudim.com.br/')
except:
    print('Não foi possível acessar o site.')
else:
    print('Site encontrado! Abrindo...')
    open('http://www.pudim.com.br/')
