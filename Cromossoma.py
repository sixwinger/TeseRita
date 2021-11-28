import pandas as pd

def funcConstrucaoCarrinhas(pop,dictConstrangimentos, dictVariavelAlgoritmo, mVolumesDados):

    carrinha = 0
    cromossoma = pop['Cromossoma 0']
    distCarrinha = funcIniciaCarrinha()
    mResultado = pd.DataFrame()
    lista = []

    for i in range(len(pop)-1):                                        #Ciclo que vai criar os cromossoma

        mCarrinha =pd.DataFrame()

        if dictConstrangimentos['Volume_Max'] >= distCarrinha['VolumeAtual']+int(mVolumesDados.loc[[cromossoma[0]]]['Volumes'])*dictConstrangimentos['Vcx']:
         
            distCarrinha['VolumeAtual'] = distCarrinha['VolumeAtual']+int(mVolumesDados.loc[[cromossoma[i]]]['Volumes']) 
            print(carrinha)
            print(distCarrinha['VolumeAtual'])
            lista.append(cromossoma[i])
        else:

            carrinha += 1
            distCarrinha = funcIniciaCarrinha()
            nome = 'Carrinha' + str(carrinha)
            mCarrinha[nome]=lista
            mResultado = pd.concat([mResultado, mCarrinha], axis=1)

    mResultado.to_excel("Dados/Cromossoma_debug.xlsx",index = True, header = True) 

    return carrinha

def funcIniciaCarrinha ():

    dictCarrinha =  {

        'VolumeAtual' : 0
        
    }
    return dictCarrinha

if __name__ == "__main__":

    print('Cromossoma fuction')