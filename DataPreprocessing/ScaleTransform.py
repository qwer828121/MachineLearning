'''
資料標準化、範圍化
StandardScaler:平均為0 標準差為1
MinMaxScaler: 最大為1 最小為0

訓練資料使用fit_transform
測試資料使用transform

X_train & X_test 可針對不同列使用不同轉換
'''

from sklearn.preprocessing import StandardScaler
st_scalar = StandardScaler()
X_train = st_scalar.fit_transform(X_train)
X_test = st_scalar.transform(X_test)

from sklearn.preprocessing import MinMaxScaler
m_scalar = MinMaxScaler()
X_train = m_scalar.fit_transform(X_train)
X_test = m_scalar.transform(X_test)

