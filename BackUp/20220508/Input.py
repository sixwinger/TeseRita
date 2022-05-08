import pandas as pd
import math as Math
print('A juntar informação Inicial')

def funcVarAlogritmo():

    dictVariavelAlgoritmo={

        'tamanho_Pop': 84,              #Tamanho da população
        'taxa_Mutacao': 1.000,          #Taxa de mutação
        'tipo_Cruzamento': 'AEX'        #tipo de cruzamento
    }

    return dictVariavelAlgoritmo

def funcConstrangimentos():

    dictConstrangimentos={
        'Vcx' : 0.5,                    #Volumetria da caixa em m3
        'Volume_Max': 50,               #Volume maximo                
        'vel_Carrinha' : 1 ,            #Velocidade em km/m da carrinha
        'tempo_entrega_volume' : 2,     #Tempo de entrega por volume
        'hora_Arranque' : 615,          #Hora de arranque
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