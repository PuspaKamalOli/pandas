import numpy as np
import pandas as pd

# concatenate:join dataframes vertically
dt_1 = pd.DataFrame({"A": [1, 2, 3],
                     "B": [4, 5, 6]
                     }, index=[1, 2, 3])
dt_2 = pd.DataFrame({"A": [7, 8, 9],
                     "C": [10, 11, 12]

                     }, index=[4, 5, 6])
print(pd.concat([dt_1, dt_2]))

# merge:join horizontally and need one column same
dt_3 = pd.DataFrame({"A": [10, 20, 30],
                     "B": [40, 50, 60],
                     'key': [1, 2, 3]
                     }, index=[1, 2, 3])
dt_4 = pd.DataFrame({"A": [70, 80, 90],
                     "C": [100, 110, 120],
                     'key': [1, 2, 3]
                     })
dt_5 = pd.merge(dt_4, dt_3, how='right', on='key')
print(dt_5)

dt_1 = pd.DataFrame({"A": [1, 2, 3],
                     "B": [4, 5, 6]
                     })
dt_2 = pd.DataFrame({"D": [7, 8, 9],
                     "E": [10, 11, 12]

                     })
print(dt_1.join(dt_2, how='left'))
