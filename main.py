from Input import *
from Initpop import *
from Cromossoma import *

mDistancias, mVolumesDados = funcDadosExcel('Dados/Distancias.xlsx' ,'Dados/Volumes.xlsm') 
dictConstrangimentos = funcConstrangimentos()
dictVariavelAlgoritmo = funcVarAlogritmo()
popInicial = funcInitPop(dictVariavelAlgoritmo['tamanho_Pop'])
mResultados = []

for cromossoma in popInicial:

    print('A validar cromossoma: ' + cromossoma)
    mCromossoma = popInicial[cromossoma].values.tolist()

    mResultados.append(funcConstrucaoCarrinhas(popInicial, dictConstrangimentos, dictVariavelAlgoritmo, mVolumesDados, mCromossoma, mDistancias))

with pd.ExcelWriter('Dados/Debug/Cromossoma_debug.xlsx') as writer:

    for nCromossoma, mResultado in enumerate(mResultados):

        nomeFolha = 'Cromossoma' + str(nCromossoma)
        mResultado.to_excel(writer,index = True, header = True, sheet_name = nomeFolha) 

if __name__ == "__main__":

    print('-- Fim --')   