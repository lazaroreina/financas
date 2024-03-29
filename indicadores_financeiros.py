# importando biliotecas

import pandas as pd 
import numpy as np 
# import pandas_datareader.data as pdd 
from acao import Acao 
import time

empresa  = Acao(ticker='SLCE3.SA')
empresa.get_values()
empresa.get_indicadores()

table = pd.Series(empresa.values_indicadores)
for c in range(3):
    print('.')
    time.sleep(1)

print('\n')
print('*'*40)
print(table)
print('*'*40)
