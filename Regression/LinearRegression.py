'''
線性回歸
使用sklearn及statsmodels.api兩種方式
差異在於X是否需要自行添加截距項
'''

#sklearn 會自行產生截距項
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train) #訓練

y_pred = regressor.predict(X_test) #預測

print('Intercept: \n', regressor.intercept_)  #輸出截距項
print('Coefficients: \n', regressor.coef_)    #輸出係數

#statsmodels.api 需自行添加截距項
import statsmodels.api as sm

X_train = sm.add_constant(X_train) #增加截距項
model = sm.OLS(y_train, X_train).fit() #訓練

X_test = sm.add_constant(X_test) #增加截距項
predictions = model.predict(X_test) #預測

model.summary()  #綜合結果
model.params     #迴歸係數
