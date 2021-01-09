# Sobre o uso da API

- Foi feito o registro no site [AccuWeather](https://developer.accuweather.com/) para conseguir uma chave da API seguindo os passos abaixo:

Após o registro ir em **MY APPS**

![my apps](img/ex0037-0.png)

Adicione uma nova aplicação e preencha as informações requisitadas. Em seguida, clique no nome da sua aplicação para pegar a chave da API.

![detalhes da app](img/ex0037-1.png)

![chave da api](img/ex0037-2.png)

----

## Pegando o código do local

Agora vá em **API PREFERENCE** e em **LOCATIONS API**.

![preferências da api](img/ex0037-3.png)

Vá em **Geoposition Search**

![api de localização](img/ex0037-4.png)

Preencha os parâmetros como a chave da API, longitude e latitude, e linguagem

![parâmetros da api](img/ex0037-5.png)

E clique no botão para enviar a requisição. Se estiver tudo funcionando, ele retornará 200.

![resposta da requisição](img/ex0037-6.png)

Vá até a **aba cURL** e pegar a url que está entre aspas.

![url](img/ex0037-7.png)

Essa url será usada no código com as devidas modificações.

----

## Pegando o tempo e o clima do local

Agora vá em **API PREFERENCE** e em **CURRENT CONDITIONS API**.

![current conditions](img/ex0037-8.png)

![current conditions](img/ex0037-9.png)

Preencha o valor das chaves da localização e API e da linguagem, conforme a imagem

![preenchendo parâmetros](img/ex0037-10.png)

E então clique para enviar a requisição. 

A seguinte imagem aparecerá com o resultado da requisição

![resposta da requisição](img/ex0037-11.png)

Vá até a **aba cURL** e pegar a url que está entre aspas.

![url](img/ex0037-12.png)

Essa url será usada no código com as devidas modificações.
