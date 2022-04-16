import pandas as pd
from AEXcruzamento import *
from Mutacao import *
from random import random

def funcCasamento (mFitnessGeral, mPop, dictVariavelAlgoritmo):

    print('A calcular Casamento')

    mPopNova = pd.DataFrame()
    for i in range(len(mPop)):

        pais = [funcSelecaoPais(mFitnessGeral),funcSelecaoPais(mFitnessGeral)]
        filho = funCruzamento(pais, mPop.copy(), dictVariavelAlgoritmo)
        print('Cruzamento Cromossoma: ' + str(i))
        nome = 'Cromossoa ' + str(i)
        mPopNova = pd.concat([mPopNova.copy(), (pd.DataFrame(filho, columns= [nome]))], axis=1)

    return mPopNova

def funcSelecaoPais(mFitnessGeral):

    valor = random()
    for i in range(len(mFitnessGeral)):

        if mFitnessGeral.iat[i,7] > valor:

            pai = mFitnessGeral.iat[i,0]
            break 
    return pai

def funCruzamento(pais, mPop, dictVariavelAlgoritmo):
 
    pais ={
        
        'pai' : mPop[pais[0]].to_list(),
        'mae' : mPop[pais[1]].to_list()
       }

    if dictVariavelAlgoritmo['tipo_Cruzamento'] == 'AEX':
        filho = funcAexcruzamento(pais)

    taxa_Mutacao = randrange(1000)/1000
    if taxa_Mutacao < dictVariavelAlgoritmo['taxa_Mutacao']:
        filho = funcMutancao(filho)

    return filho

if __name__ == "__main__":

    from Input import *    
    dictVariavelAlgoritmo = funcVarAlogritmo()
    mFitnessGeral = pd.read_excel ('Dados/Debug/Cromossoma_debug.xlsx', sheet_name='Fitness Resultado', index_col=0)
    mPop = pd.read_excel ('Dados/Debug/Data_debug.xlsx', index_col=0)

    mPopNova = funcMainCruzamento(mFitnessGeral, mPop, dictVariavelAlgoritmo)
    
    print ("-- Casamento Fim --")