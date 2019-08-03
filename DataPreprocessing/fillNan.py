
'''
填補遺漏值
代碼X部分，可以選擇需填補的列
例如將X->X[:,2:5]，即為填補2~4列
strategy除了'mean'，還有'median'、'most_frequent'
'''

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X)  
X = imputer.transform(X)
