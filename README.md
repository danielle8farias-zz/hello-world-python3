# Exercícios solucionados com Python

---

Para rodar é preciso ter o Python instalado na máquina:

- [Instalando o Python 3.8 e o IDLE no Linux](https://github.com/danielle8farias/notas-estudos/blob/main/linux/p0017_instalando_python3.8.md)

Navege até o diretório onde estão os arquivos .py e digite, no terminal:

```
$ python3.8 <nome_do_script.py>
```

- $ indica que você deve usar o usuário comum para fazer essa operação;
- a versão do python pode ser diferente da invocada acima;
- digite o nome do arquivo sem os sinais de menor e maior **< >**.

---

## Testes

Para executar os testes, primeiro instale o Pytest

```
pip install -U pytest
```

> é preciso ter o Python previamente instalado para usar o comando **pip**

Os arquivos de teste são aqueles terminados em 

```
algumacoisa_test.py
```

Para rodar **todos os testes** de um diretório, chame o terminal dentro dele e digite:

```
pytest
```

Caso queira rodar cada arquivo individualmente,

```
pytest nomedoarquivo_test.py
```

---

## Índice

- [ex0000:](ex0000_boas_vindas) Captura o nome da pessoa e retorna uma mensagem de boas-vindas na tela.

- [ex0001:](ex0001_soma_numeros) Descrição: Usuário digita dois números inteiros e programa retorna a soma entre eles.

