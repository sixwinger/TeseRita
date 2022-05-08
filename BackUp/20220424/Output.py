from Input import *
from Initpop import *
from Cromossoma import *
from Fitness import *
from Roleta import *
from Casamento import *
from Resumo import *

import pandas as pd

def funcOutput(dCromossoma, dCarrinhas):

    with pd.ExcelWriter('Dados/Debug/Resumo/Resumo.xlsx') as writer:

        nomeFolha = 'Resumo'
        dCromossoma.to_excel(writer,index = True, header = True, sheet_name = nomeFolha) 

    counter = 0
    nomeFicheiro = 'Dados/Debug/Resumo/Cromossomas 0-50.xlsx'

    for nGerecao, dCarrinha in enumerate(dCarrinhas):

        with pd.ExcelWriter(nomeFicheiro) as writer:

            nomeFolha = 'Geração ' + str(nGerecao)
            dCarrinha.to_excel(writer,index = True, header = True, sheet_name = nomeFolha) 
            counter +=1

        if counter == 50:
    
            nomeFicheiro = 'Dados/Debug/Resumo/Cromossomas ' + str(nGerecao+counter) + '-' + str(nGerecao+counter+counter) + '.xlsx'
            counter = 0

    return 0

if __name__ == "__main__":

    print('-- Fim --') 