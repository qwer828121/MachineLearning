'''
轉換類別型資料為數值型
有大小相關的使用LabelEncoder
無大小相關的使用OneHotEncoder
X可選擇需轉換列  ex: X->X[:,2]
'''

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder_X = LabelEncoder()
X = labelencoder_X.fit_transform(X)

onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()
#非數字的話，需先LabelEncoder，在OneHotEncoder
#替代方式
import pandas as pd
X = pd.get_dummies(X)
