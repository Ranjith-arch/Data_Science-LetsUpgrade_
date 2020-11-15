# Name : Yogi Halgunaki
# Assignment no : 4 (Que 3)

# Questions 3:
# How to convert the index of a series into a column of a dataframe ?

import pandas as pd

my_series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9])
print("Series is :", my_series)

print("index of a series into a column of a data frame :", my_series.to_frame().reset_index())


# Output :
# /home/yogi/Desktop/Python_Code/venv/bin/python /home/yogi/Desktop/Python_Code/Lets_Upgrade_Assignments/Day4/Day4_Que3.py
# Series is :
# 0     1
# 1     2
# 2     3
# 3     4
# 4     5
# 5     6
# 6     7
# 7     8
# 8     9
# 9     3
# 10    4
# 11    5
# 12    6
# 13    7
# 14    8
# 15    9
# 16    2
# 17    3
# 18    4
# 19    5
# 20    6
# 21    7
# 22    8
# 23    9
# dtype: int64
# index of a series into a column of a data frame :     index  0
# 0       0  1
# 1       1  2
# 2       2  3
# 3       3  4
# 4       4  5
# 5       5  6
# 6       6  7
# 7       7  8
# 8       8  9
# 9       9  3
# 10     10  4
# 11     11  5
# 12     12  6
# 13     13  7
# 14     14  8
# 15     15  9
# 16     16  2
# 17     17  3
# 18     18  4
# 19     19  5
# 20     20  6
# 21     21  7
# 22     22  8
# 23     23  9
#
# Process finished with exit code 0
