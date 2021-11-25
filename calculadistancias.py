import pandas as pd
import math as Math

def func_matriz_distancias(coord):

    data = coord['Morada']                                                      #Nome do indice da primeira Coluna
    distancias = pd.DataFrame(data = data)                                      #Inicia Coluna
    distancias.loc[-1] = ['Morada']                                             #Dá nome da coluna (para se remocer o indice no excel)
    distancias.index = distancias.index + 1                                     #Adiciona ao indices
    distancias = distancias.sort_index()                                        #ordena por indice

    for i in range(len(coord)):                                                 #Ciclo for do tamanho do ficheiro de coordenadas

        nome = 'Morada ' + str(i)                                               #Nome da Coluna (1 por encomenda)
        lista = [0] * (len((coord))+1)                                          #Criar lista de 0 do tamanho do total de encomendas
        lista[0] = coord['Morada'][i]                                           #Adiciona morada da encomenda da chegada chegada
        lat1 = coord['Latitude'][i]                                             #Latidude do ponto de partida
        long1 = coord['Longitude'][i]                                           #Longitude do ponto de partida

        for k in range(len(coord)):                                             #Ciclo for por cada encomenda possivel

            lat2 = coord['Latitude'][k]                                         #Latidude do ponto de chegada
            long2 = coord['Longitude'][k]                                       #Longitude do ponto de partida
            lista[k+1] = func_calculo_distancia(lat1,long1,lat2,long2)          #Chama função de calculo com os pontos anterios
            
        distancias[nome] = lista                                                #Adiciona a lista
    
    return distancias


def func_calculo_distancia(lat1,long1,lat2,long2): #Calculo de distancias baseadas da longitude e latitude de dois pontos

    R = 6371e3
    φ1 = lat1 * Math.pi/180
    φ2 = lat2 * Math.pi/180
    Δφ = (lat2-lat1) * Math.pi/180
    Δλ = (long2-long1) * Math.pi/180

    a = Math.sin(Δφ/2) * Math.sin(Δφ/2) + Math.cos(φ1) * Math.cos(φ2) * Math.sin(Δλ/2) * Math.sin(Δλ/2)
    c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a))

    d = R * c / 1000

    return d

if __name__ == "__main__":

    caminhoFicheiro ='coordenadasInes2.xlsm'                                #Caminho para o ficheiro com as coordenadas
    coord = pd.read_excel (caminhoFicheiro)                                 #Abre ficheiro e carrega como dataframe
    distancias = func_matriz_distancias(coord)                              #Cálculo de distancias
    distancias.to_excel("distancias.xlsx",index=False, header = False)      #Guarda no excel



