'''
Programa que tenha a função notas() que pode receber várias notas de alunos e vai retornar um
dicionário com as informações: quantidade de notas, maior nota, menor nota, média da turma,
a situação (opcional).
Adicionar também docstrings.
'''
from mensagem import cabecalho
from mensagem import rodape

cabecalho('notas dos alunos')

def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos. Aceita várias.
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre as notas da turma.
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


#testando
resp = notas(9.5, 5.5, 4, 3.7, sit=True)
print(resp)
print()
help(notas)

rodape()