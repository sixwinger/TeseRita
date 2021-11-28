import pandas as pd

def funcConstrucaoCarrinhas(pop,dictConstrangimentos, dictVariavelAlgoritmo, mVolumesDados,mCromossoma, mDistancias):
    i=0
    dictCarrinha = funcIniciaCarrinha(0, dictConstrangimentos)
    mResultado = pd.DataFrame()

    while(len(mCromossoma)!=0):                                       
    
        bTestePesoVolumes = funcTestePesoVolumes(dictConstrangimentos,dictCarrinha,mVolumesDados, mCromossoma,i)
        bTesteHorasSlot, km = funcTesteHorasSlot(dictConstrangimentos, dictCarrinha, mVolumesDados, mCromossoma, mDistancias, i)

        if bTestePesoVolumes == True and bTesteHorasSlot == True:
         
            dictCarrinha['VolumeAtual'] = dictCarrinha['VolumeAtual']+int(mVolumesDados.loc[[mCromossoma[i]]]['Volumes'])*dictConstrangimentos['Vcx'] 
            
            if dictCarrinha['horaAtual'] > mVolumesDados['Início Slot'][i]: #se a hora atual for superior à hora da slot
            
                dictCarrinha['horaAtual'] = dictCarrinha['horaAtual'] + km/dictConstrangimentos['vel_Carrinha'] + int(mVolumesDados.loc[[mCromossoma[i]]]['Volumes'])*dictConstrangimentos['tempo_entrega_volume'] 

            else: #se a hora atual for inferior à hora da slot

                dictCarrinha['horaAtual'] = mVolumesDados['Início Slot'][i] + km/dictConstrangimentos['vel_Carrinha'] + int(mVolumesDados.loc[[mCromossoma[i]]]['Volumes'])*dictConstrangimentos['tempo_entrega_volume'] 

            dictCarrinha['km'] = dictCarrinha['km'] + km

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
        
        km = mDistancias.loc[0][mCromossoma[i]+2]
        tempo = dictConstrangimentos['vel_Carrinha']

    else:
        
        km = mDistancias.loc[mCromossoma[i-1]+1][mCromossoma[i]+2]
        tempo = dictConstrangimentos['vel_Carrinha']

    if dictCarrinha['VolumeAtual']==0:

        bTesteHorasSlot = True

    elif ((mVolumesDados['Início Slot'][mCromossoma[i]] < dictCarrinha['horaAtual']+tempo) and (mVolumesDados['Fim Slot'][mCromossoma[i]] > dictCarrinha['horaAtual']+tempo)):
        
        bTesteHorasSlot = True

    else:

        bTesteHorasSlot = False
 
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