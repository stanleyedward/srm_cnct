import pandas as pd
from pathlib import Path
path = Path.home()
# print(str(path)+'/srm_cnct/connect/details.csv')

# import numpy as np
data = pd.read_csv(str(path)+'/srm_cnct/connect/details.csv', header = None)
# data = pd.read_csv(r'$HOME/srm_cnct/connect/details.csv', header = None)

# print(cwd+'/connect/details.csv')
USERNAME = data.iloc[0,0]
PASSWORD = data.iloc[0,1] 


# print(USERNAME.dtype)

# print(USERNAME)
# print(PASSWORD)