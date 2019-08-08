'''
支持向量迴歸
使用支持向量迴歸，建議先將X.Y做標準化或規一化
可以看DataPreprocessing的ScaleTransform.py
下面以標準化為例
SVR內參數可調整
kernel: 'linear'，'poly'，'rbf'，'sigmoid'，'precomputed'
C: 懲罰項 越大越容易overfittin
gamma: 越大，支持向量越少，越小，支持向量越多
'''

#標準化
from sklearn.preprocessing import StandardScaler
scaler_X = StandardScaler()
scaler_Y = StandardScaler()
X = scaler_X.fit_transform(X)
Y = scaler_Y.fit_transform(Y.reshape(-1,1))

# SVR訓練
from sklearn.svm import SVR
SVR_regressor = SVR(kernel = 'rbf')
SVR_regressor.fit(X_train, Y)

# SVR預測，預測完的Y記得轉換回來
X_test = scaler_X.transform(X_test)
y_pred = SVR_regressor.predict(X_test)
y_pred = scaler_Y.inverse_transform(y_pred)
