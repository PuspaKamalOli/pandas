import numpy as np
import pandas as pd

arr_1 = np.array([[12, 22, 32], [11, 21, 31], [13, 23, 33]])
dt_frame = pd.DataFrame(arr_1, [1, 2, 3], ['D', "E", 'F'])
print(dt_frame)

# select column
print(dt_frame['D'])

# select multiple columns
print(dt_frame[['D', 'E']])

# select row
print(dt_frame.loc[1])
print(dt_frame.iloc[1])
print(dt_frame.loc[[1, 2], ['D', 'E']])

# adding column
dt_frame['total'] = dt_frame['D'] + dt_frame['E'] + dt_frame['F']
print(dt_frame)

# adding row
dict = {'D': 14,
        'E': 24,
        'F': 34}
ser = pd.Series(dict, name='G')
dt_frame.append(ser)
print(dt_frame)

# set_index
print(dt_frame.set_index('total', inplace=True))

# assign
print(dt_frame.assign(div=dt_frame['F'] / dt_frame['E']))

# combining dataframes
dt_1 = pd.DataFrame({'A': [9, np.nan, np.nan, 12]})
dt_2 = pd.DataFrame({'A': [14, 10, 11, 13]})
print(dt_1.combine_first(dt_2))

# deleting column
print(dt_frame.drop('D', axis=1, inplace=True))
print(dt_frame)

# deleting column

print(dt_frame.drop(66, axis=0, inplace=True))
print(dt_frame)
