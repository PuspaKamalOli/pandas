import numpy as np
import pandas as pd

# series
ar = np.array(['apple', 'orange', 'mango', 'grapes'])
indx = np.array([1, 2, 3, 4])
print(pd.Series(data=ar, index=indx, name='fruits'))

# dataframe from array
ar_1 = np.array([['apple', 'football', 'cat'],
                 ['banana', 'cricket', 'dog'],
                 ['grapes', 'basketball', 'tiger']])
dt_frame = pd.DataFrame(ar_1, [1, 2, 3], ['fruits', 'sports', 'animals'])
print(dt_frame)

# dataframe from dictionary
d = {'ones': pd.Series([11, 111, 111], index=[1, 2, 3]),
     'twos': pd.Series([22, 222, 222], index=[1, 2, 3])}
print(pd.DataFrame(d))

# data frame in single line
d_1 = pd.DataFrame.from_dict(dict([("a", [1, 2, 3]), ('b', [4, 5, 6])]),orient='index',columns=['c','d','e'])
print(d_1)