# -*- coding: utf-8 -*-
#python 2 ou python 3

# Como Usar execute: python heic-to-jpg.py

'''
sudo add-apt-repository ppa:strukturag/libheif
sudo apt-get update
sudo apt-get install libheif-examples
'''

import subprocess, os, sys
from os import listdir
from os.path import isfile, join

try:
    subprocess.call(['heif-convert'])
    subprocess.call(['clear'])
    try:
        pathatual = os.getcwd()
        files = [f for f in listdir(pathatual) if isfile(join(pathatual, f))]
        for file in files:
            (nome, ext) = os.path.basename(file).split('.')

            if ext == 'heic' or ext == 'HEIC':
                destino = nome + '.jpg'
                origem = file
                print(destino)
                print(origem)
                try:
                    subprocess.call(['heif-convert', origem, destino])
                except:
                    print("Erro ao Executar o Script no Arquivo: %s", origem)
    except:
        print("Erro ao Executar o Script")
except:
    print("Voce precisa instalar o pacote libheif-examples")
    print("sudo apt-get install libheif-examples")
    print("Caso não encontre o pacote insira o repositorio")
    print("sudo add-apt-repository ppa:strukturag/libheif")
    print("sudo apt-get update")
    print("sudo apt-get install libheif-examples")

