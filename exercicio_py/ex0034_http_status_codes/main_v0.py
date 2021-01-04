########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Programa retorna o status code de um site informado pelo usuário
########

import requests

def ver_status_site(site):
    r = requests.get(site)
    return r.status_code


if __name__ == '__main__':
    #chamadas da função
    print(ver_status_site('https://danielle8farias.github.io/'))
    print(ver_status_site('https://danielle8farias.github.io/blog/'))
