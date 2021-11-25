import pandas as pd
import math as Math

def funcDadosExcel(caminhoFicheiroDistancias,caminhoFicheiroDados):

    mDistancias = pd.read_excel (caminhoFicheiroDistancias)
    mDados = pd.read_excel (caminhoFicheiroDados)
    
    return mDistancias, mDados 

def funcConstrangimentos():

    dictConstrangimentos={
        'cap_Carrinha' : 3500,          #Peso em KG da carrinha
        'Vcx' : 0.5,                    #Volumetria da caixa em m3
        'Volume_Max': 50,               #Volume maximo                
        'vel_Carrinha' : 50,            #Velocidade em km/h da carrinha
        'tempo_entrega_volume' : 2,     #Tempo de entrega por volume
        'peso_Volume' : 8,              #Peso caixa
        'hora_Arranque' : 615,          #Hora de arranque
        'hora_Final': 840
    }

    return dictConstrangimentos

if __name__ == "__main__":

    caminhoFicheiroDistancias ='Dados/Distancias.xlsx' 
    caminhoFicheiroDados = 'Dados/Dados.xlsm' 
    mDistancias, mDados = funcDadosExcel(caminhoFicheiroDistancias, caminhoFicheiroDados)
    dictConstrangimentos = funcConstrangimentos()

    print('Input Main')