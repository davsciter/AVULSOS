#!/bin/python3

import math
import os
import random
import re
import sys
import time
from threading import Thread

from os import system
thread_running = True

#Algumas brincadeiras que transformavam um decimal em binário, somava 1 bit e depois retornava o decimal

def my_forever_while():
    global thread_running
    while thread_running:
        time.sleep(0.5)
        print(".", end="", flush=True)

def changeAds(base10):
    aux=base10
    array=[]

    #Dec to binary
    while(aux>=0):
        if(aux==1 or aux==0):
            array.insert(0,aux%2)
            break
        array.insert(0,aux%2)
        aux-=((aux//2)+aux%2)
    binario = ''
    for i in array:
        binario+=str(i)
    print('Binário:',binario)

    #Invertendo bit
    for value in range(0,len(array)): 
        if(array[value]==1):
            array[value]=0
        else:
            array[value]=1

    binario = ''
    for i in array:
        binario+=str(i)
    print('Complemento de 1:',binario)


    #Somando 1 ao valor invertido
    somador = 1
    aux=[]
    for i in range(len(array)-1, -1, -1):
        if (len(array)==1 and array[i] == 1): #caso 0 gambiarra
            aux.insert(0,0)
            aux.insert(0,1)
            break
        if array[i] == 1 and somador == 1:
            aux.insert(0,0)
            somador=1
        elif array[i] == 1 and somador == 0 or array[i] == 0 and somador == 1:
            aux.insert(0,1)
            somador=0
        elif array[i] == 0 and somador == 0:
            aux.insert(0, array[i])   

    resultado = 0

    binario = ''
    for i in aux:
        binario+=str(i)
    print('Soma 1:',binario)

    result = ''
    for idx in range(0, len(aux)):
        resultado+=aux[idx]*(2**(len(aux)-idx-1))
    return resultado

def waitInp():
    input()
    global thread_running
    thread_running = False



if __name__ == '__main__':
    system('clear')
    try:
        base10 = int(input("Insira o Valor:").strip())
        system('clear')
        print('Valor Inserido:', base10)
        result = print("Resultado do Soma 1 em decimal:",changeAds(base10))
    except(ValueError):
        print('Valor inválido')
        pass
    print("\nPressione ENTER para finalizar", end="", flush=False)

    t1 = Thread(target=my_forever_while)
    t2 = Thread(target=waitInp)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    system('clear')