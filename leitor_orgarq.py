#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 23:29:42 2019

@author: henrique
"""


def hexa_binario(arquivo_hexa,hexa_binario):
        """
        Método que lê o arquivo inicial com os dados em hexa
        param arquivo_hexa: caminho do arquivo inicial com os numeros em hexa a ser lido
        param hexa_binario: caminho do arquivo onde será salvo os dados no formato  hexa -> binario
        :return: arquivo binario.txt com os dados formatados e em binario
        """
        lista_binario = []
        arq = open(arquivo_hexa, 'r')
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
        
def cria_cash1(numeros,zeros):
    """
    Método que cria uma lista de listas, com a pósição inicial de cada linha da cash
    param numero: quantidade total de linhas da cash, em decimal
    param zeros: quantidade de casas da linha (ex. 3 -> 000, 4 -> 0000)
    """
    cash = [[] for _ in range(numeros)]
    for i in range(numeros):
        b = hex(i)
        cash[i].append(bin(int(b, 16))[2:].zfill(zeros)) #linha indice: 0
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
    
def cria_cash2(numeros,zeros):
    """
    Método que cria uma lista de listas, com a pósição inicial de cada linha da cash
    param numero: quantidade total de linhas da cash, em decimal
    param zeros: quantidade de casas da linha (ex. 3 -> 000, 4 -> 0000)
    """
    cash = [[] for _ in range(numeros)]
    for i in range(numeros):
        b = hex(i)
        cash[i].append(bin(int(b, 16))[2:].zfill(zeros)) #linha indice: 0
        cash[i].append('') #v_cash    indice: 1
        cash[i].append('') #tag_cash  indice: 2
        cash[i].append('') #palavra0  indice: 3
        cash[i].append('') #palavra1  indice: 4
        cash[i].append('') #palavra2  indice: 5
        cash[i].append('') #palavra3  indice: 6
        cash[i].append('') #b_byte    indice: 7
        cash[i].append('') #Miss/Hit  indice: 8
            
    return(cash)
    
def cria_cash3(numeros,zeros):
    """
    Método que cria uma lista de listas, com a pósição inicial de cada linha da cash
    param numero: quantidade total de linhas da cash, em decimal
    param zeros: quantidade de casas da linha (ex. 3 -> 000, 4 -> 0000)
    """
    cash = [[] for _ in range(numeros)]
    for i in range(numeros):
        b = hex(i)
        cash[i].append(bin(int(b, 16))[2:].zfill(zeros)) #linha indice: 0
        cash[i].append('') #tag_cash  indice: 1
        cash[i].append(bin(int(b, 16))[2:].zfill(zeros)) #linha indice: 2
        cash[i].append('') #palavra0  indice: 3
        cash[i].append('') #palavra1  indice: 4
        cash[i].append('') #palavra2  indice: 5
        cash[i].append('') #palavra3  indice: 6
        cash[i].append('') #palavra4  indice: 7
        cash[i].append('') #palavra5  indice: 8
        cash[i].append('') #palavra6  indice: 9
        cash[i].append('') #palavra7  indice: 10
        cash[i].append('') #b_byte    indice: 7
        cash[i].append('') #Miss/Hit  indice: 8
           
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
         
        
        
def exercio1(lista_binario,exercicio1):
    """
    Método que faz a análise da cash 
    :param lista_binario: lista convertida de hexa para binario 
    :param exercicio1: caminho do arquivo.txt onde será salvo os dados da análise
    utiliza do método organiza_palavra para inserir os ultimos bits nas posições do bloco
    utiliza do método cria_cash para criar a cash vazia, com 16 libhas e 4 casas
    """
    cash = []
    cash = cria_cash1(16,4) #cria a cash com 16 linhas
    indice = 0
    hit = 0
    miss = 0
    arq = open(exercicio1,'w')
    arq.write('\nlinha, bit_validade, tag, palavra0, palavra1, palavra2, palavra3, palavra4, palavra5, palavra6, palavra7, bit para byte, Hit/Miss\n')
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
            miss += 1
       
        elif cash[indice][2] == tag:
            
            cash[indice][11] = b_byte
            cash[indice][12] = 'Hit'
            hit += 1
            
        arq.write('\n'+str(cash[indice])+'\n')
        
    arq.write('\nCash, resultado final: \n')
    arq.write('\nlinha, bit_validade, tag, palavra0, palavra1, palavra2, palavra3, palavra4, palavra5, palavra6, palavra7, bit para byte, Hit/Miss\n')     
    arq.write('\n'+str(cash)+'\n')    
    arq.write('\nTotal de Cash Hit:\n')
    arq.write(str(hit) +'\n')
    arq.write('Total de Cash Miss:\n')
    arq.write(str(miss))
    arq.close()
    

def exercio2(lista_binario,exercicio2):
    """
    Método que faz a análise da cash 
    :param lista_binario: lista convertida de hexa para binario 
    :param exercicio2: caminho do arquivo.txt onde será salvo os dados da análise
    utiliza do método organiza_palavra para inserir os ultimos bits nas posições do bloco
    utiliza do método cria_cash para criar a cash vazia
    """
    cash = []
    cash = cria_cash2(32,5) #cria a cash com 32
    indice = 0
    hit = 0
    miss = 0
    arq = open(exercicio2,'w')
    arq.write('\nlinha, bit_validade, tag, palavra0, palavra1, palavra2, palavra3, bit para byte, Hit/Miss\n')
    for i in range(len(lista_binario)):
        x = str(lista_binario[i])
        tag = x[0:8]
        linha  = x[8:13]
        palavra = x[0:15]
        b_byte = x[15]
        for j in range(len(cash)):
            
            if linha in cash[j]:
                indice = j #achei a linha: cash[indice] 
            
        if cash[indice][2] != tag:
            
            cash[indice][1] = '1'
            cash[indice][2] = tag
            cash[indice][3] = organiza_palavra(palavra,2)[0]
            cash[indice][4] = organiza_palavra(palavra,2)[1]
            cash[indice][5] = organiza_palavra(palavra,2)[2]
            cash[indice][6] = organiza_palavra(palavra,2)[3]
            cash[indice][7] = b_byte
            cash[indice][8] = 'Miss'
            miss += 1
       
        elif cash[indice][2] == tag:
            
            cash[indice][7] = b_byte
            cash[indice][8] = 'Hit'
            hit += 1
            
        arq.write('\n'+str(cash[indice])+'\n')
        
    arq.write('\nCash, resultado final: \n')
    arq.write('\nlinha, bit_validade, tag, palavra0, palavra1, palavra2, palavra3, bit para byte, Hit/Miss\n')     
    arq.write('\n'+str(cash)+'\n')    
    arq.write('\nTotal de Cash Hit:\n')
    arq.write(str(hit) +'\n')
    arq.write('Total de Cash Miss:\n')
    arq.write(str(miss))
    arq.close()

def exercio3(lista_binario,exercicio3):
    """
    Método que faz a análise da cash 
    :param lista_binario: lista convertida de hexa para binario 
    :param exercicio2: caminho do arquivo.txt onde será salvo os dados da análise
    utiliza do método organiza_palavra para inserir os ultimos bits nas posições do bloco
    utiliza do método cria_cash para criar a cash vazia
    palavra0, palavra1, palavra2, palavra3,palavra4, palavra5, palavra6, palavra7,
    """
    cash = []
    cash = cria_cash3(16,4) #cria a cash com 16 linhas
    hit = 0
    miss = 0
    cont2 = 0
    arq = open(exercicio3,'w')
    arq.write('\nlinha, tag, linha, palavra0, palavra1, palavra2, palavra3,palavra4, palavra5, palavra6, palavra7, bit para byte, Hit/Miss\n')
    for i in range(len(lista_binario)):
        x = str(lista_binario[i])
        tag = x[0:12]
        palavra = x[0:15]
        b_byte = x[15]
        cont = 0
        
        for k in range(len(cash)):
            if cash[k][1] != '':
                cont += 1
        
        if cont == len(cash) and tag not in cash:
            cash[cont2][1] = tag
            cash[cont2][3] = organiza_palavra(palavra,3)[0]
            cash[cont2][4] = organiza_palavra(palavra,3)[1]
            cash[cont2][5] = organiza_palavra(palavra,3)[2]
            cash[cont2][6] = organiza_palavra(palavra,3)[3]
            cash[cont2][7] = organiza_palavra(palavra,3)[4]
            cash[cont2][8] = organiza_palavra(palavra,3)[5]
            cash[cont2][9] = organiza_palavra(palavra,3)[6]
            cash[cont2][10] = organiza_palavra(palavra,3)[7]
            cash[cont2][11] = b_byte
            cash[cont2][12] = 'Miss'
            miss += 1
            if cont2 < len(cash):
                cont2 += 1
            else:
                cont2 = 0
            cont = 0
            
        else:
            for j in range(len(cash)):
                if tag == cash[j][1]:
                    cash[j][11] = b_byte
                    cash[j][12] = 'Hit'
                    hit += 1
                    break
            
                elif cash[j][1] == '':
                    cash[j][1] = tag
                    cash[j][3] = organiza_palavra(palavra,3)[0]
                    cash[j][4] = organiza_palavra(palavra,3)[1]
                    cash[j][5] = organiza_palavra(palavra,3)[2]
                    cash[j][6] = organiza_palavra(palavra,3)[3]
                    cash[j][7] = organiza_palavra(palavra,3)[4]
                    cash[j][8] = organiza_palavra(palavra,3)[5]
                    cash[j][9] = organiza_palavra(palavra,3)[6]
                    cash[j][10] = organiza_palavra(palavra,3)[7]
                    cash[j][11] = b_byte
                    cash[j][12] = 'Miss'
                    miss += 1
                    break
               
        arq.write('\n'+str(cash[j])+'\n')
        
    arq.write('\nCash, resultado final: \n')
    arq.write('\nlinha, tag, linha, palavra0, palavra1, palavra2, palavra3, palavra4, palavra5, palavra6, palavra7, bit para byte, Hit/Miss\n') 
    arq.write('\n'+str(cash)+'\n')    
    arq.write('\nTotal de Cash Hit:\n')
    arq.write(str(hit) +'\n')
    arq.write('Total de Cash Miss:\n')
    arq.write(str(miss))
    arq.close()              
            
    
    
    

if __name__ == "__main__":
    
    lista_binario = hexa_binario('/home/henrique/orgarqt3/orgarqT3/arquivo_hexa','/home/henrique/orgarqt3/orgarqT3/hexa_binario')    

    #Mapeamento direto, com 8 bits para tag, 4 bits para linha, 3 bits
    #para palavra e 1 bit para byte (cache com 16 linhas, 8 palavras por linha).
    exercio1(lista_binario,'/home/henrique/orgarqt3/orgarqT3/exercicio1')
    
    
    #Mapeamento direto, com 8 bits para tag, 5 bits para linha, 2 bits
    #para palavra e 1 bit para byte (cache com 32 linhas, 4 palavras por linha).
    exercio2(lista_binario,'/home/henrique/orgarqt3/orgarqT3/exercicio2')
    
    
    #Mapeamento associativo, com 12 bits para tag, 3 bits para palavra
    #e 1 bit para byte (cache com 16 linhas, 8 palavras por linha).
    exercio3(lista_binario,'/home/henrique/orgarqt3/orgarqT3/exercicio3')
    
    #Mapeamento associativo, com 13 bits para tag, 2 bits para palavra 
    #e 1 bit para byte (cache com 32 linhas, 4 palavras por linha).
    
    
    
    
    
    
    