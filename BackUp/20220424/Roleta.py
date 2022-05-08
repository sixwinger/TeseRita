import pandas as pd
import numpy as np

def funcRoleta (fitnessGeral):

    num = len(fitnessGeral)
    factor = fitnessGeral['Resultado Fitness'].sum()

    fitnessGeral['%'] = fitnessGeral['Resultado Fitness'] / factor
    resultadoRoleta = funcOrdenaRoleta(fitnessGeral, num)


    return resultadoRoleta 

def funcOrdenaRoleta(fitnessGeral, num):

    print('A calcular Roleta')

    resultadoRoleta = fitnessGeral.sort_values(by='%', ascending=False)
    resultadoRoleta['% Acumulada'] = list(np.arange(1,num+1))

    for i in range(num):

        if i == 0:

            resultadoRoleta.iat[i,7] = resultadoRoleta.iat[i,6]  

        else:
            
            resultadoRoleta.iat[i,7] = resultadoRoleta.iat[i-1,7] +resultadoRoleta.iat[i,6]
    
    return resultadoRoleta 


if __name__ == "__main__":

    fitnessGeral = pd.read_excel ('Dados/Debug/Fitness_Debug.xlsx', sheet_name='Fitness Resultado', index_col=0)
    resultadoRoleta = funcRoleta(fitnessGeral) 

    with pd.ExcelWriter('Dados/Debug/Roleta_Debug.xlsx') as writer:

        nomeFolha = 'Roleta Resultado'
        resultadoRoleta.to_excel(writer,index = True, header = True, sheet_name = nomeFolha) 
    print('-- Roleta Main Fim --') 