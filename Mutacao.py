import pandas as pd
import numpy as np
from random import randrange

def funcMutancao(cromossoma):

   print(cromossoma)
   i = randrange(len(cromossoma)-1)
   j = randrange(i+1,len(cromossoma))
   novoCromossoma = cromossoma.copy()
   print(str(i) + ":" + str(j))

   while i<j:

      print(cromossoma[i])
      print(cromossoma[j])
      novoCromossoma[i] = cromossoma[j] 
      novoCromossoma[j] = cromossoma[i] 

      i+=1      
      j-=1

   print(novoCromossoma)
   return novoCromossoma

if __name__ == "__main__":

    cromossoma = [3, 9, 5, 2, 6, 4, 1, 7, 8]
    filho = funcMutancao(cromossoma)

    print('-- Fim Mutação --')   