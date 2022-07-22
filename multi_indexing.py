import numpy as np
import pandas as pd

ar_1 = np.array(['A', 'A', "C"])
ar_2 = np.array(['C', "D", "E"])
ar_3 = np.array([[10, 20, 30], [90, 33, 45], [23, 98, 76]])
tup_1 = pd.MultiIndex.from_tuples(list(zip(ar_1, ar_2)))

dt_frame = pd.DataFrame(ar_3, tup_1, ['x', 'y', 'z'])
print(dt_frame)
# elements under row A
print(dt_frame.loc['A'])
# elements of row A and under C
print(dt_frame.loc['A'].loc['C'])
# elements of row A and column x
print(dt_frame.loc["A"]['x'])
# creates dataframe of row A separately
print(dt_frame.xs('A'))
