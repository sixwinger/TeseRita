import pandas as pd
from AEXcruzamento import *
from Mutacao import *
import random

def funcCasamento (mRoleta, mPop, dictVariavelAlgoritmo):

    print('A calcular Casamento')

    mPopNova = pd.DataFrame()
    for i in range(len(mPop)+1):

        pais = [funcSelecaoPais(mRoleta, dictVariavelAlgoritmo['tipo_Selecao']),funcSelecaoPais(mRoleta, dictVariavelAlgoritmo['tipo_Selecao'])]
        filho = funCruzamento(pais, mPop.copy(), dictVariavelAlgoritmo)
        nome = 'Cromossoma ' + str(i)
        mPopNova = pd.concat([mPopNova.copy(), (pd.DataFrame(filho, columns= [nome]))], axis=1)

    return mPopNova

def funcSelecaoPais(mRoleta, tipo_Selecao):


    if tipo_Selecao == 'Rank':

        valor = random()
        for i in range(len(mRoleta)):

            if mRoleta.iat[i,7] > valor:

                pai = mRoleta.iat[i,0]
                break 

    if tipo_Selecao == 'Torneio':

        concorrente_1 = random.randint(0, len(mRoleta)-1)
        concorrente_2 = random.randint(0, len(mRoleta)-1)
        while concorrente_1 == concorrente_2:

            concorrente_2 = random.randint(0, len(mRoleta))

        if mRoleta.iat[concorrente_1,5] > mRoleta.iat[concorrente_2,5]:

            pai = mRoleta.iat[concorrente_1,0]
        else:

            pai = mRoleta.iat[concorrente_2,0]

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
    mRoleta = pd.read_excel ('Dados/Debug/Cromossoma_debug.xlsx', sheet_name='Fitness Resultado', index_col=0)
    mPop = pd.read_excel ('Dados/Debug/Data_debug.xlsx', index_col=0)

    mPopNova = funcCasamento(mRoleta, mPop, dictVariavelAlgoritmo)
    
    print ("-- Casamento Fim --")