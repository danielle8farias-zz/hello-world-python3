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

- [ex0000:](exercicio_py/ex0000_boas_vindas) Captura o nome da pessoa e retorna uma mensagem de boas-vindas na tela.

- [ex0001:](exercicio_py/ex0001_soma_numeros) Descrição: Usuário digita dois números inteiros e programa retorna a soma entre eles.

- [ex0002:](exercicio_py/ex0002_tabuada_multiplicacao) Usuário digita dois números inteiros e programa retorna a tabuada de multiplicação desse.

- [ex0003:](exercicio_py/ex0003_lista_frutas) Usuário informa nome de cinco frutas. O programa armazena numa lista e retorna em ordem alfabética.

- [ex0004:](exercicio_py/ex0004_conta_quantidade_caractere) Usuário informa nome e sobrenome. O programa retorna quantas letras o nome completo possui (excluindo espaços) e quantas letras o primeiro nome possui. 

- [ex0005:](exercicio_py/ex0005_aumento_salario) Usuário informa o salário de uma pessoa. O programa retorna um reajuste de aumento desse salário.

- [ex0006:](exercicio_py/ex0006_obrigatoriedade_voto) Usuário informa a idade e programa retorna se o voto é obrigatório.

- [ex0007:](exercicio_py/ex0007_progressao_aritmetica) Usuário informa o 1º termo de uma progressão aritmética e sua razão. O programa retorna os 10 primeiros termos dessa PA.

- [ex0008:](exercicio_py/ex0008_palindromo) Usuário informa uma palavra ou frase e programa retorna se ela é um palíndromo.

- [ex0009:](exercicio_py/ex0009_adivinha_numero) Jogo de adivinhação de números.

- [ex0010:](exercicio_py/ex0010_fatorial) Usuário informa um número inteiro e programa retorna o seu fatorial.

- [ex0011:](exercicio_py/ex0011_media_maior_menor_num) Usuário informa diversos números inteiros. O programa deve retornar a média desses números, qual o menor deles e o maior.

- [ex0012:](exercicio_py/ex0012_fibonacci) Sequência Fibonacci.

