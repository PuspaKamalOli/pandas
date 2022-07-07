import numpy as np
import pandas as pd

arr_1 = np.array([[12, 5, 13],
                  [15, 12, 18],
                  [100, 500, 300]])
dt_frame = pd.DataFrame(arr_1, ["C", "D", 'E'], ["A", "B", "C"])
print(dt_frame)

# iterating dataframe
for label, ser in dt_frame.items():
    print(label, ser)
for index, row in dt_frame.iterrows():
    print(index, row)
for row in dt_frame.itertuples():
    print(row)

# sorting dataframe
print(dt_frame.sort_values(by='B'))
print(dt_frame.sort_index(ascending=True))
