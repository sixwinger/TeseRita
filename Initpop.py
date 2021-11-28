import pandas as pd
import random
from Input import *
print('A iniciar população Inicial')
def funcInitPop(volumes):                                           #Inicia nova população

    data = range(1,volumes)                                       #Cria o range do tamanho do numero de entregas + partida + chegada
    pop = pd.DataFrame()                                            #Inicia data frame do pandas

    for i in range(volumes):                                        #Ciclo que vai criar os cromossoma

        nome = 'Cromossoma '+ str(i)                                 #Atribui o nome do cromossoma
        lista = random.sample(range(0, volumes-1), volumes-1)       #Gera uma matriz aliatoriamente de 2 até tamanho de população 1 
        pop[nome] = lista                                           #Adiciona o cromossoma há população
    
    pop.to_excel("Dados/Debug/Data_debug.xlsx",index = True, header = True) 
    return pop

if __name__ == "__main__":

    dictVariavelAlgoritmo = funcVarAlogritmo()
    popInicial = funcInitPop(dictVariavelAlgoritmo['tamanho_Pop'])
    popInicial.to_excel("Dados/Debug/Data_debug.xlsx",index = True, header = True) 
   
    print('Init fuction')