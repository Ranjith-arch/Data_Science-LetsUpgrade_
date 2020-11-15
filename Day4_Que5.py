# Name : Yogi Halagunaki
# Assignment No : 4 (Que 5)

# Questions 5:
# Which country origin cars are a part of this dataset?

import seaborn as sb
import pandas as pd
data_set = sb.load_dataset('mpg')
print(data_set)

df = pd.DataFrame(data_set)
print(" country origin :", df.origin.unique())

# Output :
# /home/yogi/Desktop/Python_Code/venv/bin/python /home/yogi/Desktop/Python_Code/
# Lets_Upgrade_Assignments/Day4/Day4_Que5.py
#       mpg  cylinders  ...  origin                       name
# 0    18.0          8  ...     usa  chevrolet chevelle malibu
# 1    15.0          8  ...     usa          buick skylark 320
# 2    18.0          8  ...     usa         plymouth satellite
# 3    16.0          8  ...     usa              amc rebel sst
# 4    17.0          8  ...     usa                ford torino
# ..    ...        ...  ...     ...                        ...
# 393  27.0          4  ...     usa            ford mustang gl
# 394  44.0          4  ...  europe                  vw pickup
# 395  32.0          4  ...     usa              dodge rampage
# 396  28.0          4  ...     usa                ford ranger
# 397  31.0          4  ...     usa                 chevy s-10
#
# [398 rows x 9 columns]
#  country origin : ['usa' 'japan' 'europe']
#
# Process finished with exit code 0
