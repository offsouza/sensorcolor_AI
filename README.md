#  Análise de Fluidos utilizando algoritmo de Aprendizado de Máquina.

Este é um projeto onde é feito um aprendizado supervisionado no sensor , onde através de coleta de dados emitido pelo sensor classificamos e armazenamos esse dados, para que o algoritimo reconheça padrões no dados e depois através de um teste cego o algoritmo verifica quais dados a amostra teste se aproxima e a classifica de acordo com o banco.

## Requisitos
###### Bibliotecas Utilizadas: 

>from scipy.stats import mode  || pip install scipy

>import serial  ||  pip install pyserial 

>import numpy as np || pip install numpy

>import csv  || Já vem como padrão

>import sys  || Já vem como padrão

>import time  || Já vem como padrão


## Obtenção dos Dados 

A captura dos dados é feita pela serial, ou seja, é preciso que as informações do sensor chegam pela serial. É preciso colocar a porta que está sendo transmitido os dados no código ` py_colorimetroV5.py ` dentro da função `def ino ` presente no script. 

## Armazenamento dos Dados 

É os dados são gravados em um arquivo .csv em que é possível alterar o nome do arquivo mudando a segunda linha de código da função def __init__ . Onde como padrão o nome é `colorimetroteste1.csv`.


## Sensor

Este arquivo tem como foco a análise dos dados, ou seja, o código em python. Logo, não abordarei  qual sensor e microcontrolador utilizei no projeto. Porém qualquer um irá funcionar, basta que coloque os dados separados por vírgulas. 

contato: otaviosouza3m@hotmail.com






