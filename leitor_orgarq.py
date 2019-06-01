#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 23:29:42 2019

@author: henrique
"""


def hexa_binario(arquivo,arquivo_pronto):
        """
        Método que lê o arquivo inicial com os dados em hexa
        param arquivo: arquivo inicial a ser lido
        cria um arquivo_pronto.txt com os dados do arquivo em binario
        """
        arq = open(arquivo, 'r')
        arq2 = open(arquivo_pronto,'w')
        arquivo = arq.readlines()
        a = []
        for i in range(len(arquivo)):
            a.append(arquivo[i].split(','))
            for j in range(len(a[i])):
                b = ((a[i][j]).strip())
                if b != '':
                    x = bin(int(b, 16))[2:].zfill(16)
                    arq2.write(b +' --> '+x +'\n')
        arq.close()
        arq2.close()                  
      
def cria_numeros_cash_8b(numeros):
    """
    Método que converte um inteiro para Hexa de 8 bits
    param numero: quantidade total de posições da cash, em decimal
    """
    for i in range(numeros):
        b = hex(i)
        x = bin(int(b, 16))[2:].zfill(8)
        print(x)
            




if __name__ == "__main__":
    
    hexa_binario('/home/henrique/orgarqt3/orgarqT3/arquivo','/home/henrique/orgarqt3/orgarqT3/arquivo_pronto')    
    
    cria_numeros_cash_8b(256)
    
    
    
    
    
    
    