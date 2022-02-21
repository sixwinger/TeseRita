import pandas as pd
import numpy as np

def funcCalculoFitness(mFitness):

    print('A Calcular Fitness')
    num = len(mFitness)
    
    fit = pd.DataFrame(list(np.arange(1,num+1)),columns=['Pontuação KM'])
    fit = fit.sort_values(by='Pontuação KM', ascending=False)
    fitnessKM = mFitness[['Cromossoma', 'km']].sort_values(by='km', ascending=True)
    fitnessKM['Pontuação KM'] = fit.values
    
    fit = pd.DataFrame(list(np.arange(1,num+1)),columns=['Pontuação NCarrinhas'])
    fit = fit.sort_values(by='Pontuação NCarrinhas', ascending=False)
    fitnessNCarrinhas = mFitness[['Cromossoma', 'Carrinhas']].sort_values(by='Carrinhas', ascending=True)
    fitnessNCarrinhas['Pontuação NCarrinhas'] = fit.values 
 
    fitnessGeral = mFitness.join(fitnessKM['Pontuação KM'])
    fitnessGeral = fitnessGeral.join(fitnessNCarrinhas['Pontuação NCarrinhas'])

    fitnessGeral['Resultado Fitness'] = fitnessGeral['Pontuação KM'] + fitnessGeral['Pontuação NCarrinhas']

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
    fitnessGeral = funcCalculoFitness(mFitness)
    print('-- Fitness Main Fim --')  