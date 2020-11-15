# Name : Yogi Halagunaki
# Assignment no: 4(Que 2)

# Questions 2:
# How to create a series from a numpy array?

import numpy as np

import pandas as pd

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 91, 2, 4, 5, 8, 9, 6, 5, 4, 3, 2, 5])
print("Array of numpy is :", arr)

print("Series of pandas is :", pd.Series(arr))

# Output :
# Array of numpy is : [ 1  2  3  4  5  6  7  8 91  2  4  5  8  9  6  5  4  3  2  5]
# Series of pandas is : 0      1
# 1      2
# 2      3
# 3      4
# 4      5
# 5      6
# 6      7
# 7      8
# 8     91
# 9      2
# 10     4
# 11     5
# 12     8
# 13     9
# 14     6
# 15     5
# 16     4
# 17     3
# 18     2
# 19     5
# dtype: int64

# Process finished with exit code 0
