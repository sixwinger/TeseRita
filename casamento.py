import pandas as pd
from random import random
def funcSelecaoPais(mFitnessGeral):

    valor = random()
    for i in range(len(mFitnessGeral)):

        if mFitnessGeral.iat[i,7] > valor:

            pai = mFitnessGeral.iat[i,0]
            print(valor)
            print(pai)
            break 
    return pai

def funCasamento(pais,mPop):

    pai = mPop[pais[0]]
    mae = mPop[pais[1]]

    return cromossoma


if __name__ == "__main__":

    
    mFitnessGeral = pd.read_excel ('Dados/Debug/Cromossoma_debug.xlsx', sheet_name='Fitness Resultado', index_col=0)
    mPop = pd.read_excel ('Dados/Debug/Data_debug.xlsx', index_col=0)
    pais = [funcSelecaoPais(mFitnessGeral),funcSelecaoPais(mFitnessGeral)]
    funCasamento(pais, mPop)
    print (pais)
    print ("-- Casamento Fim --")