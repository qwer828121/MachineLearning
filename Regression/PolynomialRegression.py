'''
多項式回歸
本質上也是線性迴歸
只是先將X進行次方轉換後，再線性迴歸
degree 為 次方次數
'''

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 3)   #degree可以改變
X_poly = poly_reg.fit_transform(X_train)
linea_model = LinearRegression()
linea_model.fit(X_poly, Y)    #訓練

#預測，需先多項式轉換後，線性回歸預測
linea_model.predict(poly_reg.fit_transform(X_test)) 
