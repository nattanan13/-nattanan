# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 20:36:03 2021

@author: Acer
"""

import numpy as np
import pandas as pd
# Val1 have "None" 
val1 = np.array([1, None, 3, 4])
val1
val1.dtype
val1.sum()
val1.sum(), val1.min(), val1.max()


# Val2 have np.nan
val2 = np.array([1, np.nan, 3, 4])
val2
val2.dtype
val2.sum()

val2.sum(), val2.min(), val2.max()
np.nansum(val2)
np.nanmin(val2)
np.nanmax(val2)

pd.Series([1, np.nan, 2, None])
x = pd.Series(range(2), dtype = int)
x
# 0    0
# 1    1
x[0] = None
x
# 0    NaN
# 1    1.0
