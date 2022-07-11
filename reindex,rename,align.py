import pandas as pd
import numpy as np

# align
dt_fm1 = pd.DataFrame([[10, 20], [11, 22]],
                      [1, 2],
                      ['a', 'b'])
dt_fm2 = pd.DataFrame([[10, 20], [11, 22]],
                      [3, 4],
                      ['a', 'b'])

print(dt_fm1.align(dt_fm2))

# reindexing
dt_fm3 = pd.DataFrame([[10, 20, 30], [11, 22, 33]],
                      [1, 2],
                      ['a', 'b', 'c'])
print(dt_fm3.reindex(['x', 'y']))

# rename
print(dt_fm3.rename(columns={'a': 'x', 'b': 'y', 'c': 'z'}))
