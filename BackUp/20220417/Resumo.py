import pandas as pd
import re

def funcResumo(mResultado, mRoleta, dCromossoma, dCarrinhas):

    dCromossoma = pd.concat([dCromossoma, mRoleta.iloc[0]], ignore_index=True, axis = 1)

    nCromossoma = int(re.search(r'\d+', mRoleta.iloc[0][0]).group())
    dCarrinhas.append(mResultado[nCromossoma])

    return dCromossoma, dCarrinhas




if __name__ == "__main__":

    mRoleta = pd.read_excel ('Dados/Debug/mRoleta_Debug.xlsx', sheet_name='Roleta Resultado', index_col=0)