import numpy as np
import pandas as pd

a_1 = np.array([[1, 2, 3],
                [np.nan, 20, 30],
                [100, 200, 300],
                [145, np.nan, 70],
                [324, 765, np.nan],
                [334, 789, 900],
                [np.nan, 88, 77]])
dt_frame = pd.DataFrame(a_1,
                        ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
                        ['X', "Y", 'Z'])
print(dt_frame)

# first 5 elements
print(dt_frame.head())

# last 5 elemts
print(dt_frame.tail())

# indexing
print(dt_frame[0:7:2])

# index in array
print(dt_frame.index)

# all the columns
print(dt_frame.columns)

# converts to numpy
print(dt_frame.to_numpy())

# fill empty columns by integer
print(dt_frame.fillna(0))

# edit each columns
print(dt_frame.transform([lambda x: x + 10]))

# edit selected columns
print(dt_frame.transform({'X': lambda x: x * 10,
                          "Y": lambda x: x + 100,
                          "Z": lambda x: x * 100}))

# edit selected column and print it only
print(dt_frame['X'].map(lambda x: x + 20))
