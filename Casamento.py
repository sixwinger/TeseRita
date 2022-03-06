import pandas as pd
from AEXcruzamento import *
from Mutacao import *
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

def funCasamento(pais,mPop, dictVariavelAlgoritmo):

    pais ={
        
        'pai' : mPop[pais[0]].to_list(),
        'mae' : mPop[pais[1]].to_list()
       }

    filho = funcAexcruzamento(pais)
    taxa_Mutacao = randrange(1000)/1000
    if taxa_Mutacao < dictVariavelAlgoritmo['taxa_Mutacao']:
        print(taxa_Mutacao)
        filho = funcMutancao(filho)

    return filho

# juntar um filho numa matrix e criar a função mae
if __name__ == "__main__":

    from Input import *    
    dictVariavelAlgoritmo = funcVarAlogritmo()
    mFitnessGeral = pd.read_excel ('Dados/Debug/Cromossoma_debug.xlsx', sheet_name='Fitness Resultado', index_col=0)
    mPop = pd.read_excel ('Dados/Debug/Data_debug.xlsx', index_col=0)
    pais = [funcSelecaoPais(mFitnessGeral),funcSelecaoPais(mFitnessGeral)]
    funCasamento(pais, mPop, dictVariavelAlgoritmo)
    print (pais)
    print ("-- Casamento Fim --")