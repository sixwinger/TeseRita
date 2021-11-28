import pandas as pd

def funcConstrucaoCarrinhas(pop,dictConstrangimentos, dictVariavelAlgoritmo, mVolumesDados,mCromossoma, mDistancias):
    i=0
    dictCarrinha = funcIniciaCarrinha(0, dictConstrangimentos)
    mResultado = pd.DataFrame()

    while(len(mCromossoma)!=0):                                        #Ciclo que vai criar os mCromossoma
    
        bTestePesoVolumes = funcTestePesoVolumes(dictConstrangimentos,dictCarrinha,mVolumesDados, mCromossoma,i)
        bTesteHorasSlot, tempoViagem = funcTesteHorasSlot(dictConstrangimentos, dictCarrinha, mVolumesDados, mCromossoma, mDistancias, i)

        if bTestePesoVolumes == True and bTesteHorasSlot == True:
         
            dictCarrinha['VolumeAtual'] = dictCarrinha['VolumeAtual']+int(mVolumesDados.loc[[mCromossoma[i]]]['Volumes'])*dictConstrangimentos['Vcx'] 
            
            if dictCarrinha['horaAtual'] > mVolumesDados['Início Slot'][i]:
            
                dictCarrinha['horaAtual'] = dictCarrinha['horaAtual'] + tempoViagem + int(mVolumesDados.loc[[mCromossoma[i]]]['Volumes'])*dictConstrangimentos['tempo_entrega_volume'] 

            else:

                dictCarrinha['horaAtual'] = mVolumesDados['Início Slot'][i] + tempoViagem + int(mVolumesDados.loc[[mCromossoma[i]]]['Volumes'])*dictConstrangimentos['tempo_entrega_volume'] 

            

            dictCarrinha['lista'].append(mCromossoma[i])
            del mCromossoma[i]

        else:

            i+=1

        if len(mCromossoma)<=i:

            i = 0
            #print(dictCarrinha['VolumeAtual'])
            #print(dictCarrinha['horaAtual'])
            mResultado = funcEscreveCarrinha(mResultado, dictCarrinha)
            dictCarrinha = funcIniciaCarrinha(dictCarrinha['Carrinha'], dictConstrangimentos)

    return mResultado 

def funcTestePesoVolumes(dictConstrangimentos, dictCarrinha,mVolumesDados,mCromossoma,i):

    if (dictConstrangimentos['Volume_Max'] >= dictCarrinha['VolumeAtual']+int(mVolumesDados.loc[[mCromossoma[i]]]['Volumes'])*dictConstrangimentos['Vcx']):
        
        bTestePesoVolumes = True

    else:

        bTestePesoVolumes = False
 
    return bTestePesoVolumes

def funcTesteHorasSlot(dictConstrangimentos, dictCarrinha,mVolumesDados,mCromossoma,mDistancias,i):

    if i == 0:
        
        tempo = mDistancias.loc[0][mCromossoma[i]+2]/dictConstrangimentos['vel_Carrinha']

    else:
        
        tempo = mDistancias.loc[mCromossoma[i-1]+1][mCromossoma[i]+2]/dictConstrangimentos['vel_Carrinha']

    if dictCarrinha['VolumeAtual']==0:

        bTesteHorasSlot = True

    elif ((mVolumesDados['Início Slot'][mCromossoma[i]] < dictCarrinha['horaAtual']+tempo) and (mVolumesDados['Fim Slot'][mCromossoma[i]] > dictCarrinha['horaAtual']+tempo)):
        
        bTesteHorasSlot = True

    else:

        bTesteHorasSlot = False
 
    return bTesteHorasSlot, tempo

def funcIniciaCarrinha (carrinha, dictConstrangimentos):

    dictCarrinha =  {

        'Carrinha'      : carrinha + 1,
        'VolumeAtual'   : 0,
        'lista'         : [],
        'horaAtual' : dictConstrangimentos['hora_Arranque'] 
    }
    return dictCarrinha

def funcEscreveCarrinha (mResultado, dictCarrinha):

    nome = 'Carrinha ' + str(dictCarrinha['Carrinha'])
    mCarrinha =pd.DataFrame([dictCarrinha['VolumeAtual'],dictCarrinha['horaAtual']],columns=[nome], index =['Volume','Hora Final'])
    lista_df = pd.DataFrame()
    lista_df[nome] = dictCarrinha['lista']
    mCarrinha = mCarrinha.append(lista_df)
    mResultado = pd.concat([mResultado, mCarrinha], axis=1)

    return mResultado

if __name__ == "__main__":

    print('Cromossoma fuction')