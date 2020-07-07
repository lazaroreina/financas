# importando biliotecas

import pandas as pd 
import numpy as np 
# import pandas_datareader.data as pdd 
from acao import Acao 


empresa  = Acao(ticker='LREN3.SA')
empresa.get_values()

print(empresa.ticker, '\n', empresa.values_ativo)
print(empresa.values_passivo)
print(empresa.values_indicadores)








