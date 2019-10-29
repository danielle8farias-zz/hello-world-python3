'''
Pergunte a distância de uma viagem em Km e calcule o preço da passagem
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens
mais longas.
'''
#importando parte do código
from mensagem import cabecalho
from mensagem import rodape

#função que calcula o preço da passagem
def f_preco(distancia):
    if distancia <= 200:
        preco = distancia * 0.5
    else:
        preco = distancia * 0.45
    #:.2f limita o número de duas casas decimais
    print(f'Preço da passagem R${preco:.2f}')

#programa principal
cabecalho('PREÇO DA PASSAGEM')
#1º laço fazendo o programa rodar até que o usuário decida parar
while True:
    distancia = float(input('Qual a distância da viagem?(Km) '))
    f_preco(distancia)
    print()
    resposta = ' '
    #2º laço enquanto a resposta não for S ou N
    while resposta not in 'SN':
        #upper: joga a string para maiúsculo
        #strip: remove os espaços no começo e no fim
        #[0] captura apenas o primeiro caractere
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
    print()
    if resposta == 'N':
        #quebrando o 1º laço
        break
rodape()
