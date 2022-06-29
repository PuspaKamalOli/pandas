import pandas as pd
import numpy as np

ar_1 = np.array([[10, 100, 1000],
                 [20, 200, 2000],
                 [30, 300, 3000]])
dt_frame = pd.DataFrame(ar_1, ['D', 'E', 'F'], ["A", 'B', 'C'])
print(dt_frame)

# checks condition:return true or false

print(dt_frame > 800)
print(dt_frame['A'] < 800)
# greater than
print(dt_frame.gt(1000))
# less than
print(dt_frame.lt(1000))
# greater or equal to
print(dt_frame.ge(1000))
# less than or equal to
print(dt_frame.le(1000))
# equals to
print(dt_frame.eq(100))
# not equal to
print(dt_frame.ne(300))

# return elements of column that satisfy condition
print(dt_frame[dt_frame['A'] >= 20])
# return the column B and C with correspondance condition satisfied
print(dt_frame[dt_frame['A'] <= 200][['B', 'C']])
# checks multiple conditions for a column
print(dt_frame[(dt_frame['B'] > 100) & (dt_frame['B'] < 300)])
