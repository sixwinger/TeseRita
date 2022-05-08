#teste

from Input import *
from Initpop import *
from Cromossoma import *
from Fitness import *
from Roleta import *
from Casamento import *
from Resumo import *
from Output import *
import pandas as pd


mDistancias, mVolumesDados = funcDadosExcel('Dados/Distancias.xlsx' ,'Dados/Volumes.xlsm') 
dictConstrangimentos = funcConstrangimentos()
dictVariavelAlgoritmo = funcVarAlogritmo()
popInicial = funcInitPop(dictVariavelAlgoritmo['tamanho_Pop'])
mResultados = []
mFitness = pd.DataFrame()
dCromossoma = pd.DataFrame()
dCarrinhas = []

itry = 1
ftry = 4

while itry != ftry:

    print('Geração: ' + str(itry))
    for cromossoma in popInicial:

        print('A validar cromossoma: ' + cromossoma)
        mCromossoma = popInicial[cromossoma].values.tolist()

        mResultado = funcConstrucaoCarrinhas(popInicial, dictConstrangimentos, dictVariavelAlgoritmo, mVolumesDados, mCromossoma, mDistancias)
        mFitness = pd.concat([mFitness,(pd.DataFrame([[str(cromossoma), mResultado.loc['km'].sum(),mResultado.loc['km'].count()]], columns = ['Cromossoma','km','Carrinhas']))], ignore_index='True')
        mResultados.append(mResultado)

    mFitnessGeral = funcFitnessAdaptada(mFitness.copy())
    mRoleta = funcRoleta(mFitnessGeral)

    mNewpop = funcCasamento(mFitnessGeral, popInicial.copy() , dictVariavelAlgoritmo)

    popInicial = mNewpop.copy()
    mFitness = pd.DataFrame()
    itry += 1
    dCromossoma, dCarrinhas = funcResumo(mResultados,mRoleta,dCromossoma.copy(), dCarrinhas)

    if itry != ftry:
        mResultados = []

with pd.ExcelWriter('Dados/Debug/Cromossoma_debug.xlsx') as writer:

    nomeFolha = 'Fitness'
    mFitness.to_excel(writer,index = True, header = True, sheet_name = nomeFolha) 

    nomeFolha = 'Fitness Resultado'
    mFitnessGeral.to_excel(writer,index = True, header = True, sheet_name = nomeFolha) 

    for nCromossoma, mResultado in enumerate(mResultados):

        nomeFolha = 'Cromossoma' + str(nCromossoma)
        mResultado.to_excel(writer,index = True, header = True, sheet_name = nomeFolha) 

with pd.ExcelWriter('Dados/Debug/Roleta_Debug.xlsx') as writer:

    nomeFolha = 'Roleta Resultado'
    mRoleta.to_excel(writer,index = True, header = True, sheet_name = nomeFolha) 

with pd.ExcelWriter('Dados/Debug/Cruzamento_debug.xlsx') as writer:

    nomeFolha = 'Cruzamento Resultado'
    mNewpop.to_excel(writer,index = True, header = True, sheet_name = nomeFolha) 

funcOutput(dCromossoma, dCarrinhas)

if __name__ == "__main__":

    print('-- Fim --')   