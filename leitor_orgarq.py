#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 23:29:42 2019

@author: henrique
"""


def hexa_binario(arquivo,hexa_binario):
        """
        Método que lê o arquivo inicial com os dados em hexa
        param arquivo: arquivo inicial a ser lido
        cria um arquivo_pronto.txt com os dados do arquivo em binario
        """
        lista_binario = []
        arq = open(arquivo, 'r')
        arq2 = open(hexa_binario,'w')
        arquivo = arq.readlines()
        a = []
        for i in range(len(arquivo)):
            a.append(arquivo[i].split(','))
            for j in range(len(a[i])):
                b = ((a[i][j]).strip())
                if b != '':
                    x = bin(int(b, 16))[2:].zfill(16)
                    lista_binario.append(x)
                    arq2.write(b +' --> '+x +'\n')
                    
        arq.close()
        arq2.close()
        return(lista_binario)
        
def cria_linha_cash(numeros):
    """
    Método que cria uma lista de listas, com a pósição inicial de cada linha da cash
    param numero: quantidade total de posições da cash, em decimal
    """
    cash = [[] for _ in range(numeros)]
    for i in range(numeros):
        b = hex(i)
        cash[i].append(bin(int(b, 16))[2:].zfill(4)) #linha indice: 0
        cash[i].append('') #v_cash    indice: 1
        cash[i].append('') #tag_cash  indice: 2
        cash[i].append('') #palavra0  indice: 3
        cash[i].append('') #palavra1  indice: 4
        cash[i].append('') #palavra2  indice: 5
        cash[i].append('') #palavra3  indice: 6
        cash[i].append('') #palavra4  indice: 7
        cash[i].append('') #palavra5  indice: 8
        cash[i].append('') #palavra6  indice: 9
        cash[i].append('') #palavra7  indice: 10
        cash[i].append('') #b_byte    indice: 11
        cash[i].append('') #Miss/Hit  indice: 12
            
    return(cash)
    

def organiza_palavra(palavra,ultimos_bits):
    """
    Método que organiza a palavra 
    :param palavra: string: palavra a ser lida. ex: 00000111 
    :param ultimos_bits: int: tamanho em decimal, dos ultimos bits a serem retornados.Ex. 3 == 111
    :return: lista de ultimos bits organizados em sequencia binaria. ex. [000,001,010...]
    """  
    lista_ultimos_bits = []
    u = len(palavra) - ultimos_bits
    y = (palavra[0:u])
    for i in range(2**ultimos_bits):
        b = (hex(i))
        c = (bin(int(b, 16))[2:].zfill(ultimos_bits))
        lista_ultimos_bits.append(y+c)
        
    return(lista_ultimos_bits)
        
    
    
        
        
def exercio1(lista_binario,arquivo_pronto):
    cash = []
    cash = cria_linha_cash(16)
    indice = ''
    arq = open(arquivo_pronto,'w')
    for i in range(len(lista_binario)):
        x = str(lista_binario[i])
        tag = x[0:8]
        linha  = x[8:12]
        palavra = x[0:15]
        b_byte = x[15]
        
        for j in range(len(cash)):
            
            if linha in cash[j]:
                indice = j #achei a linha: cash[indice] 
            
        if cash[indice][2] != tag:
            
            cash[indice][1] = '1'
            cash[indice][2] = tag
            cash[indice][3] = organiza_palavra(palavra,3)[0]
            cash[indice][4] = organiza_palavra(palavra,3)[1]
            cash[indice][5] = organiza_palavra(palavra,3)[2]
            cash[indice][6] = organiza_palavra(palavra,3)[3]
            cash[indice][7] = organiza_palavra(palavra,3)[4]
            cash[indice][8] = organiza_palavra(palavra,3)[5]
            cash[indice][9] = organiza_palavra(palavra,3)[6]
            cash[indice][10] = organiza_palavra(palavra,3)[7]
            cash[indice][11] = b_byte
            cash[indice][12] = 'Miss'
       
        elif cash[indice][2] == tag:
            
            cash[indice][12] = 'Hit'
            cash[indice][11] = b_byte
            
           
        print('cash[indice]:')    
        print(cash[indice])
        arq.write('bit_validade, tag, palavra0, palavra1, palavra2, palavra3, palavra4, palavra5,palavra6, palavra7, bit para byte, Hit / Miss')
        arq.write('\n'+str(cash[indice])+'\n')
        
    
    arq.close()            
            
    
    
    

if __name__ == "__main__":
    
    lista_binario = hexa_binario('/home/henrique/orgarqt3/orgarqT3/arquivo','/home/henrique/orgarqt3/orgarqT3/hexa_binario')    
    
    exercio1(lista_binario,'/home/henrique/orgarqt3/orgarqT3/arquivo_pronto')
    
    #print(organiza_palavra('000000000101000',3)[7])
    
    
    
    
    