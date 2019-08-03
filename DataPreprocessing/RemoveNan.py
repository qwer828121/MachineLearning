'''
移除遺漏值
使用前，需先檢查遺漏值數量
在考慮填補或移除
'''

#使用pandas dropna
import pandas as pd
X = X.dropna(axis=0)  #axis=1為刪除列

#使用numpy.isnan()，注意X需皆為數字
X = X[~np.isnan(X).any(axis=1)]
