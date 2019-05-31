#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 23:29:42 2019

@author: henrique
"""


def leitura_pergaminho(arquivo,arquivo_pronto):
        """
        Método que lê o arquivo inicial
        param arquivo: arquivo inicial a ser lido
        return: retorna uma lista com os dados do arquivo
        """
        arq = open(arquivo, 'r')
        arq2 = open(arquivo_pronto,'w')
        arquivo = arq.readlines()
        a = []
        c = []
        for i in range(len(arquivo)):
            a.append(arquivo[i].split(','))
            for j in range(len(a[i])):
                b = ((a[i][j]).strip())
                if b != '':
                    x = bin(int(b, 16))[2:].zfill(16)
                    arq2.write(b +' --> '+x +'\n')
        arq.close()
        arq2.close()                  
        return(c)
      
              




if __name__ == "__main__":
    
    print(leitura_pergaminho('/home/henrique/orgarqt3/arquivo','/home/henrique/orgarqt3/arquivo_pronto'))
    
    
    
    
    
    
    
    
    
    