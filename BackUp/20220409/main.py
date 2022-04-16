from Input import *
from Initpop import *
from Cromossoma import *
from Fitness import *
from Roleta import *
from Casamento import *
import pandas as pd

mDistancias, mVolumesDados = funcDadosExcel('Dados/Distancias.xlsx' ,'Dados/Volumes.xlsm') 
dictConstrangimentos = funcConstrangimentos()
dictVariavelAlgoritmo = funcVarAlogritmo()
popInicial = funcInitPop(dictVariavelAlgoritmo['tamanho_Pop'])
mResultados = []
mFitness = pd.DataFrame()


for cromossoma in popInicial:

    print('A validar cromossoma: ' + cromossoma)
    mCromossoma = popInicial[cromossoma].values.tolist()

    mResultado = funcConstrucaoCarrinhas(popInicial, dictConstrangimentos, dictVariavelAlgoritmo, mVolumesDados, mCromossoma, mDistancias)
    mFitness = pd.concat([mFitness,(pd.DataFrame([[str(cromossoma), mResultado.loc['km'].sum(),mResultado.loc['km'].count()]], columns = ['Cromossoma','km','Carrinhas']))], ignore_index='True')
    mResultados.append(mResultado)

mFitnessGeral = funcFitnessAdaptada(mFitness.copy())
mRoleta = funcRoleta(mFitnessGeral)

mNewpop = funcCasamento(mFitnessGeral, popInicial.copy() , dictVariavelAlgoritmo)


## Outputs ##
with pd.ExcelWriter('Dados/Debug/Cromossoma_debug.xlsx') as writer:

    nomeFolha = 'Fitness'
    mFitness.to_excel(writer,index = True, header = True, sheet_name = nomeFolha) 

    nomeFolha = 'Fitness Resultado'
    mFitnessGeral.to_excel(writer,index = True, header = True, sheet_name = nomeFolha) 

    for nCromossoma, mResultado in enumerate(mResultados):

        nomeFolha = 'Cromossoma' + str(nCromossoma + 1)
        mResultado.to_excel(writer,index = True, header = True, sheet_name = nomeFolha) 

with pd.ExcelWriter('Dados/Debug/Roleta_Debug.xlsx') as writer:

    nomeFolha = 'Roleta Resultado'
    mRoleta.to_excel(writer,index = True, header = True, sheet_name = nomeFolha) 

with pd.ExcelWriter('Dados/Debug/Cruzamento_debug.xlsx') as writer:

    nomeFolha = 'Cruzamento Resultado'
    mNewpop.to_excel(writer,index = True, header = True, sheet_name = nomeFolha) 

if __name__ == "__main__":

    print('-- Fim --')   