# Exercícios solucionados com Python

---

## Como rodar os scripts:

Para rodar é preciso ter o Python instalado na máquina:

- [Instalando o Python 3.8 e o IDLE no Linux](https://github.com/danielle8farias/notas-estudos/blob/main/linux/p0017_instalando_python3.8.md)

Navege até o diretório onde estão os arquivos .py e digite, no terminal:

```
$ python3.8 <nome_do_script.py>
```

- **$** indica que você deve usar o usuário comum para fazer essa operação;
- a versão do python pode ser diferente da invocada acima;
- digite o nome do arquivo sem os sinais de menor e maior **< >**.

Para saber qual versão do Python 3 está na sua máquina, digite no terminal:

```
$ python3 -V
```

## Arquivos com a shebang

É esse camaradinha aqui: 

```
#!
```

Você vai encontrá-la na primeira linha de alguns arquivos, assim:

```
#!/usr/bin/env python3.8
```

Antes de executar é preciso dar as permissões ao arquivo através do comando no terminal:

```
$ chmod +x <nome_do_arquivo.py>
```

- **chmod** vem de change mode que é quem vai fazer as mudanças;
- **+x** para adicionar as permissões de execução (e*x*ecute permission).

Para chamar o arquivo, digite:

```
$ ./<nome_do_script.py>
```

- o **ponto-barra** juntos serve para indicar o caminho do executável;
- o **ponto** significa diretório atual;
- a **barra** serve para separar o diretório do nome do arquivo.


---

## Testes:

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

## Índice:

- [ex0000:](ex0000_boas_vindas) Captura o nome da pessoa e retorna uma mensagem de boas-vindas na tela.

- [ex0001:](ex0001_soma_numeros) Descrição: Usuário digita dois números inteiros e programa retorna a soma entre eles.

- [ex0002:](ex0002_tabuada_multiplicacao) Usuário digita dois números inteiros e programa retorna a tabuada de multiplicação desse.

- [ex0003:](ex0003_lista_frutas) Usuário informa nome de cinco frutas. O programa armazena numa lista e retorna em ordem alfabética.

