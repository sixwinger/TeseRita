#Ficheiro: Fitness
#Descrição: Cálculo de Fitness dos cromossomas com base do número de carrinhas atribuidas e o número de km realizados pelo cromossoma
#Funções:
#  -- funcFitnessAdaptada --
#       Input: mFitness (variavel com o resultado da desconstrução dos cromossoma: km precorridos e número de carrinhas por cromossoma)
#       Output: fitnesssGeral - Variavel com o cálculo total de fitness na última coluna [Resultado Fitness] 
#       Algoritmo base:
#           1- Ordenar o resultado dos cromossomos por km precorrido
#           2- Atribuir a pontuação máxima ao cromossoma com menor km (pt_max = tamanho do cromossoma)
#           3- Se o proximo cromossoma tiver a mesma distancia atribuir a mesma pontuação
#           4- Se tiver uma maior distancia precorrida dar menos um ponto por cada cromossoma que tiver menos km percorridos
#           5- Ordenar o resultado dos cromossomos por numero de carrinhas (inverso)
#           6- Atribuir a pontuação máxima ao cromossoma com menor carrinhas (pt_max = tamanho do cromossoma)
#           7- Se o proximo cromossoma o mesmo número de carrinhas atribuir a mesma pontuação
#           8- Se tiver um número maior de carrinhas dar menos um ponto por cada cromossoma que tiver menos carrinhas
#           9- Somar ambas as pontuações sendo este o resultado do fitness (quanto maior melhor)

#Biliotecas

import pandas as pd
import numpy as np

#Função 
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
 
    factor = (num*(1+num))
    fitnessGeral['%'] = fitnessGeral['Resultado Fitness'] / factor
    fitnessGeral = funcOrdenaFitnessGeral(fitnessGeral, num)

    return fitnessGeral

def funcOrdenaFitnessGeral(fitnessGeral, num):

    fitnessGeral = fitnessGeral.sort_values(by='%', ascending=False)
    fitnessGeral['% Acumulada'] = list(np.arange(1,num+1))

    for i in range(num):

        if i == 0:

            fitnessGeral.iat[i,7] = fitnessGeral.iat[i,6]  

        else:
            
            fitnessGeral.iat[i,7] = fitnessGeral.iat[i-1,7] + fitnessGeral.iat[i,6]
    
    return fitnessGeral
if __name__ == "__main__":

    mFitness = pd.read_excel ('Dados/Debug/Cromossoma_debug.xlsx', sheet_name='Fitness', index_col=0)
    fitnessGeral = funcFitnessAdaptada(mFitness)
    
    with pd.ExcelWriter('Dados/Debug/Fitness_Debug.xlsx') as writer:

        nomeFolha = 'Fitness Resultado'
        fitnessGeral.to_excel(writer,index = True, header = True, sheet_name = nomeFolha) 
    print('-- Fitness Main Fim --')  