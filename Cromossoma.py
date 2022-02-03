import pandas as pd

def funcConstrucaoCarrinhas(pop,dictConstrangimentos, dictVariavelAlgoritmo, mVolumesDados,mCromossoma, mDistancias):
   
    i=0                                                         #Inicia variável que corre cromossoma
    dictCarrinha = funcIniciaCarrinha(0, dictConstrangimentos)  #Inicia carrinha
    mResultado = pd.DataFrame()                                 #Inicia data frame que vai ficar com as carrinhas
    
    #Inicia ciclo que corre enquanto houver encomendas por atribuir a carrinhas                                       
    while(len(mCromossoma)!=0): 

        #Chama funções de teste de peso e de horas de slot
        bTestePesoVolumes = funcTestePesoVolumes(dictConstrangimentos,dictCarrinha,mVolumesDados, mCromossoma,i)
        bTesteHorasSlot, km = funcTesteHorasSlot(dictConstrangimentos, dictCarrinha, mVolumesDados, mCromossoma, mDistancias, i)

        #Se poder ir na carrinha: Coloca encomenda sumando volume, tempo e km
        if bTestePesoVolumes == True and bTesteHorasSlot == True:
         
            dictCarrinha['VolumeAtual'] = dictCarrinha['VolumeAtual']+int(mVolumesDados.loc[[mCromossoma[i]]]['Volumes'])*dictConstrangimentos['Vcx'] 

            dictCarrinha['horaAtual'] = dictCarrinha['horaAtual']+km/dictConstrangimentos['vel_Carrinha']

            #se a hora atual for superior à hora da slot
            if dictCarrinha['horaAtual'] > mVolumesDados['Início Slot'][mCromossoma[i]] : 
            
                dictCarrinha['horaAtual'] = dictCarrinha['horaAtual'] + int(mVolumesDados.loc[[mCromossoma[i]]]['Volumes'])*dictConstrangimentos['tempo_entrega_volume'] 
           
            #se a hora atual for inferior à hora da slot
            else: 

                dictCarrinha['horaAtual'] = mVolumesDados['Início Slot'][mCromossoma[i]] + int(mVolumesDados.loc[[mCromossoma[i]]]['Volumes'])*dictConstrangimentos['tempo_entrega_volume'] 

            dictCarrinha['km'] = dictCarrinha['km'] + km    #soma km
            dictCarrinha['lista'].append(mCromossoma[i])    #coloca encomenda
            del mCromossoma[i]                              #retira encomenda do cromossoma
            i+=1

        #Passa para a encomenda seguite se o volume ou hora não são compativeis
        else:

            i+=1

        #Depois de correr o cromossoma todo começa de novo iniciando uma nova carrinha
        if len(mCromossoma)<=i: 

            i = 0                                                                               #Volta há posição inicial
            mResultado = funcEscreveCarrinha(mResultado, dictCarrinha)                          #Adiciona o resultado a matriz de resultados
            dictCarrinha = funcIniciaCarrinha(dictCarrinha['Carrinha'], dictConstrangimentos)   #Inicia uma nova carrinha

    #Termina função e returna a matriz de resultados
    return mResultado 

#Função que testa se o volume pode ir para a carrinha
def funcTestePesoVolumes(dictConstrangimentos, dictCarrinha,mVolumesDados,mCromossoma,i):

    #se Volume Max >= Volume da Atual + Volumes da Encomenda * Volume da Caixa
    if (dictConstrangimentos['Volume_Max'] >= dictCarrinha['VolumeAtual']+int(mVolumesDados.loc[[mCromossoma[i]]]['Volumes'])*dictConstrangimentos['Vcx']):
        
        bTestePesoVolumes = True

    else:

        bTestePesoVolumes = False
 
    return bTestePesoVolumes

def funcTesteHorasSlot(dictConstrangimentos, dictCarrinha,mVolumesDados,mCromossoma,mDistancias,i):

    #km = km de distancia entre os cromossomas
    #tempo = km de distancia x velocidade média da carrinha
    
    #se for a primeira viagem então parte do armazem
    if i == 0: 
        
        km = mDistancias.loc[0][mCromossoma[i]+2]
        tempo = dictConstrangimentos['vel_Carrinha']*km

    #se não for a primeira viagem então verifica o ultimo ponto
    else: 
        
        km = mDistancias.loc[mCromossoma[i]+1][dictCarrinha['lista'][len(dictCarrinha['lista'])-1]+2]
        tempo = dictConstrangimentos['vel_Carrinha']*km


    InicioSlot = mVolumesDados['Início Slot'][mCromossoma[i]] 
    HoraChegada = dictCarrinha['horaAtual']+tempo
    FimSlot = mVolumesDados['Fim Slot'][mCromossoma[i]] 

    #se não tiver volume então é porque é a primeira encomenda logo pode ir ao slot
    if dictCarrinha['VolumeAtual']==0: 

        bTesteHorasSlot = True

    #Se Hora do slot for inferior a hora de chegada e inferior a hora de fim de slot
    elif (( InicioSlot < HoraChegada) and (FimSlot > HoraChegada)):
        
        bTesteHorasSlot = True

    else:

        bTesteHorasSlot = False

    #Retorna o Boleano de teste de horas de slot e os km
    return bTesteHorasSlot, km

def funcIniciaCarrinha (carrinha, dictConstrangimentos):

    dictCarrinha =  {

        'Carrinha'      : carrinha + 1,
        'VolumeAtual'   : 0,
        'lista'         : [],
        'horaAtual'     : dictConstrangimentos['hora_Arranque'],
        'km'            : 0 
    }
    return dictCarrinha

def funcEscreveCarrinha (mResultado, dictCarrinha):

    nome = 'Carrinha ' + str(dictCarrinha['Carrinha'])
    mCarrinha =pd.DataFrame([dictCarrinha['VolumeAtual'],dictCarrinha['horaAtual'],dictCarrinha['km']],columns=[nome], index =['Volume','Hora Final','km'])
    lista_df = pd.DataFrame()
    lista_df[nome] = dictCarrinha['lista']
    mCarrinha = mCarrinha.append(lista_df)
    mResultado = pd.concat([mResultado, mCarrinha], axis=1)

    return mResultado

if __name__ == "__main__":

    print('Cromossoma fuction')