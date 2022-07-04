import pandas as pd
import numpy as np

a_1 = np.array([[4, 5, 6, 100],
                [40, 50, 60, 200],
                [44, 55, 66, 300],
                [46, 45, 64, 400]])
dt_frame = pd.DataFrame(a_1,
                        ['e', 'f', 'g', 'h'],
                        ['a', 'b', 'c', 'd'])
print(dt_frame)

# sum of all elements of column 's'
print(dt_frame['a'].sum())

# mean of all elements of column 'b'
print(dt_frame['b'].mean())

# median of all elements of column 'c'
print(dt_frame['c'].median())

# standard deviation of all elements of column 'd'
print(dt_frame['d'].std())

# variants of all elements of column 'd'
print(dt_frame['d'].var())

# mean of all elements of row 'e'
print(dt_frame.loc['e'].mean())

# max of all elements of row 'g'
print(dt_frame.loc['g'].max())
# skewness of all elements of row 'h'
print(dt_frame.loc['h'].skew())

# all the static representation of each columns
print(dt_frame.describe())
