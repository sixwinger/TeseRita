from Input import *
from Initpop import *
from Cromossoma import *

mDistancias, mVolumesDados = funcDadosExcel('Dados/Distancias.xlsx' ,'Dados/Volumes.xlsm') 
dictConstrangimentos = funcConstrangimentos()
dictVariavelAlgoritmo = funcVarAlogritmo()
popInicial = funcInitPop(dictVariavelAlgoritmo['tamanho_Pop'])
carrinha = funcConstrucaoCarrinhas(popInicial, dictConstrangimentos, dictVariavelAlgoritmo, mVolumesDados)

print(carrinha)

if __name__ == "__main__":

    print('Main fuction')   