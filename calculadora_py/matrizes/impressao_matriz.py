from time import sleep


#função que imprime matriz
def imprimir_matriz(M, Mi, Mj):
    for i in range(Mi):
        for j in range(Mj):
            sleep(0.5)
            print(f'[{M[i][j]:^5}]', end='', flush=True)
        print()
