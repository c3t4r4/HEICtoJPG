# Converte imagem heic para jpg
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/c3t4r4)

# Funciona em Python 2 e Python 3!

# Dependencias
  - libheif-examples
  - Linux Ubuntu, Mint ...

# - Instalando Dependencia

```sh
$ sudo apt-get install libheif-examples
```
### - Caso ocorra erro ao encontrar o pacote:

```sh
$ sudo add-apt-repository ppa:strukturag/libheif
$ sudo apt-get update
$ sudo apt-get install libheif-examples
```



### Como Usar:
  - Copiar o arquivo para a pasta onde contem os arquivos .heic ou .HEIC
  - Execute:
    ```sh 
    $ python heic-to-jpg.py 
    ```
  - Todos os arquivos da pasta serão convertidos
  - Os arquivos de origem serão mantidos