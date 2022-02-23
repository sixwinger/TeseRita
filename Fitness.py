#Ficheiro: Fitness
#Descrição: Cálculo de Fitness dos cromossomas com base do numero de carrinhas atribuidas e o numero de km realizados pelo cromossoma
#Funções:
#  -- funCalculoFitness --
#       Input: mFitness (variavel com a desconstrução dos cromossoma)
#       Output: fitnesssGeral - Variavel com o cálculo total de fitness  

import pandas as pd
import numpy as np

def funcFitnessAdaptada(fitnessGeral):

#km
    num = len(fitnessGeral)
    fitnessGeral['Pontuação KM'] = list(np.arange(1,num+1))
    numPontuação = len(fitnessGeral)
    fitnessGeral = fitnessGeral.sort_values(by='km', ascending=True)
    peso = 0    
    for i in range(num):

        if i == 0:

            fitnessGeral.iat[i,3] =numPontuação

        elif fitnessGeral.iat[i,1] == fitnessGeral.iat[i-1,1]:

            fitnessGeral.iat[i,3] = numPontuação
            peso = peso + 1
        else:

            numPontuação = numPontuação - 1 - peso
            fitnessGeral.iat[i,3] = numPontuação
            peso = 0

#num carrinhas 

    numPontuação = len(fitnessGeral)
    fitnessGeral['Pontuação NCarrinhas'] = list(np.arange(1,num+1))
    fitnessGeral = fitnessGeral.sort_values(by='Carrinhas', ascending=True)
  
    numPontuação = len(fitnessGeral)
    peso = 0
    for i in range(num):

        if i == 0:

            fitnessGeral.iat[i,4] =numPontuação

        elif fitnessGeral.iat[i,2] == fitnessGeral.iat[i-1,2]:

            fitnessGeral.iat[i,4] = numPontuação
            peso = peso + 1
        else:

            numPontuação = numPontuação - 1 - peso
            fitnessGeral.iat[i,4] = numPontuação
            peso = 0
    fitnessGeral['Resultado Fitness'] = fitnessGeral['Pontuação KM'] + fitnessGeral['Pontuação NCarrinhas']
    fitnessGeral = fitnessGeral.sort_values(by='Resultado Fitness', ascending=False)


    return fitnessGeral


if __name__ == "__main__":

    mFitness = pd.read_excel ('Dados/Debug/Cromossoma_debug.xlsx', sheet_name='Fitness', index_col=0)
    fitnessGeral = funcFitnessAdaptada(mFitness)
    
    with pd.ExcelWriter('Dados/Debug/Fitness_Debug.xlsx') as writer:

        nomeFolha = 'Fitness Resultado'
        fitnessGeral.to_excel(writer,index = True, header = True, sheet_name = nomeFolha) 
    print('-- Fitness Main Fim --')  