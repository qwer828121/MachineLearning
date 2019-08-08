'''
Ridge跟ElasticNet
這兩個迴歸帶有Regularization正規化效果
ElasticNet是LASSO跟Ridge的結合
'''

#Ridge訓練(需手動設定參數)
from sklearn.linear_model import Ridge
Ridge_regressor = Ridge(alpha=1.0)
Ridge_regressor.fit(X_train, Y)

#RidgeCV訓練(透過CV挑選參數)
from sklearn.linear_model import RidgeCV
Ridge_regressor = RidgeCV(alphas=[1e-3, 1e-2, 1e-1, 1)
Ridge_regressor.fit(X_train, Y)

#Ridge預測
y_pred = Ridge_regressor.predict(X_test)


#ElasticNet訓練(需手動設定參數)
from sklearn.linear_model import ElasticNet
ElasticNet_regressor = ElasticNet(alpha=1.0, l1_ratio=0.5)
ElasticNet_regressor.fit(X_train, Y)

#ElasticNetCV訓練(透過CV決定參數)
from sklearn.linear_model import ElasticNetCV
ElasticNet_regressor = ElasticNet(cv=5)
ElasticNet_regressor.fit(X_train, Y)

#ElasticNet預測
y_pred = ElasticNet_regressor.predict(X_test)



