import numpy as np
import pandas as pd

dict = {'A': pd.Series([200, np.nan, 300, np.nan, 500, 1000, 400, np.nan]),
        'B': pd.Series([150, np.nan, 300, 378, 400, 900, 800, np.nan]),
        'C': pd.Series([20, 45, np.nan, np.nan, 50, 100, 40, np.nan], ),
        'D': pd.Series([2, np.nan, 3, np.nan, 5, 1, 4, np.nan, np.nan]),
        'E': pd.Series([2, 10, 3, 20, 5, 1, 4, 30, 40])
        }
d_1 = pd.DataFrame(dict)

# remove row with empty data
d_2 = d_1.dropna(axis=0)
print(d_2)

# remove column with empty data
d_3 = d_1.dropna(axis=1)
print(d_3)

# remove column with empty data more than 3
d_4 = d_1.dropna(thresh=3)
print(d_4)

# update empty space with 29
d_5 = d_1.fillna(29)
print(d_5)

# update empty space with given value
d_6 = d_1.fillna(value=d_1['A'].std())
print(d_6)

# update empty space with back num
d_7 = d_1.fillna(method='bfill')
print(d_7)

# update empty space with forward num
d_8 = d_1.fillna(method='ffill')
print(d_8)
