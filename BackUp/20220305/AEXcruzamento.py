import pandas as pd
import numpy as np
from random import randrange

def funcAexcruzamento(pais):

    tamanhoFilhos = len(pais['pai'])

    filho = list(np.zeros(tamanhoFilhos, dtype=int))
    i=0
    index = 0
    flag = 'pai'

    while i < tamanhoFilhos:
               
        if i == 0:

            filho[0] = pais['pai'][0]
            filho[1] = pais['pai'][1]
            index = index + 2
            i = i + 2

        else:
            
            if flag == 'pai':

               flag = 'mae'
               j = pais[flag].index(filho[i-1])+1
               if j > (tamanhoFilhos - 1): j=0

               while pais[flag][j] in filho:

                   j = randrange(tamanhoFilhos-1)

               filho[i] = pais[flag][j]
               
            else: 
            
                flag = 'pai'
                j = pais[flag].index(filho[i-1])+1
                if j > (tamanhoFilhos - 1):
                    j=0
                while pais[flag][j] in filho:

                   j = randrange(tamanhoFilhos-1)
              
                filho[i] = pais[flag][j]
            
            index += 1
            i += 1
            print(filho)
    return filho



if __name__ == "__main__":


    pais ={

        'pai' : [3, 9, 5, 2, 6, 4, 1, 7, 8],
        'mae' : [7, 8, 1, 9, 4, 3, 5, 6, 2]
        }

    filho = funcAexcruzamento(pais)

    print(filho)
    print('-- Fim AEX --')   