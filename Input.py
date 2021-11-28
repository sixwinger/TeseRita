import pandas as pd
import math as Math

def funcVarAlogritmo():

    dictVariavelAlgoritmo={

        'tamanho_Pop': 85               #Tamanho da população
    }

    return dictVariavelAlgoritmo

def funcConstrangimentos():

    dictConstrangimentos={
        'Vcx' : 0.5,                    #Volumetria da caixa em m3
        'Volume_Max': 50,               #Volume maximo                
        'vel_Carrinha' : 50,            #Velocidade em km/h da carrinha
        'tempo_entrega_volume' : 2,     #Tempo de entrega por volume
        'hora_Arranque' : 615,          #Hora de arranque
        'hora_Final': 840
    }

    return dictConstrangimentos

def funcDadosExcel(caminhoFicheiroDistancias,caminhoFicheiroVolumes):

    mDistancias = pd.read_excel (caminhoFicheiroDistancias)
    mVolumes = pd.read_excel (caminhoFicheiroVolumes)

    return mDistancias, mVolumes 

if __name__ == "__main__":

    caminhoFicheiroDistancias ='Dados/Distancias.xlsx' 
    caminhoFicheiroVolumes = 'Dados/Volumes.xlsm' 
    mDistancias, mVolumesDados = funcDadosExcel(caminhoFicheiroDistancias, caminhoFicheiroVolumes)
    dictConstrangimentos = funcConstrangimentos()
    dictVariavelAlgoritmo = funcVarAlogritmo()

    print('Input Main')