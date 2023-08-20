import pandas as pd
# import numpy as np

data = pd.read_csv('connect/details.csv', header = None)

USERNAME = data.iloc[0,0]
PASSWORD = data.iloc[0,1] 

# print(USERNAME.dtype)

# print(USERNAME)
# print(PASSWORD)