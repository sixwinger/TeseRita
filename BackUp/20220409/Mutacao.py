import pandas as pd
import numpy as np
from random import randrange

def funcMutancao(cromossoma):

   i = randrange(len(cromossoma)-1)
   j = randrange(i+1,len(cromossoma))
   print(str(i)+':'+str(j))
   novoCromossoma = cromossoma.copy()

   while i<j:

      novoCromossoma[i] = cromossoma[j] 
      novoCromossoma[j] = cromossoma[i] 

      i+=1      
      j-=1

   return novoCromossoma

if __name__ == "__main__":

   cromossoma = [3, 9, 5, 2, 6, 4, 1, 7, 8, 15, 14, 13 ,12, 11, 10]
   filho = funcMutancao(cromossoma)
   print(filho)

   print('-- Fim Mutação --')   