import pandas as pd
import random
from Input import funcVarAlogritmo
print('A iniciar população Inicial')


def funcInitPop(volumes):               # Inicia nova população

    pop = pd.DataFrame()                # Inicia data frame do pandas

    for i in range(volumes):            # Ciclo que vai criar os cromossoma

        nome = 'Cromossoma ' + str(i)   # Atribui o nome do Cromossoma

        # Gera uma matriz aliatoriamente de 2 até tamanho de população 1

        lista = random.sample(range(0, volumes-1), volumes-1)
        lista = [x+1 for x in lista]
        pop[nome] = lista               # Adiciona o cromossoma há população

    # Debug para ficheiro excel
    pop.to_excel("Dados/Debug/Data_debug.xlsx", index=True, header=True)

    return pop


if __name__ == "__main__":

    dictVariavelAlgoritmo = funcVarAlogritmo()
    popInicial = funcInitPop(dictVariavelAlgoritmo['tamanho_Pop'])
    popInicial.to_excel("Dados/Debug/Data_debug.xlsx", index=True, header=True)

    print('Init fuction')
