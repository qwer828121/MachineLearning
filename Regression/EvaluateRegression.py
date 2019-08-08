'''
介紹幾個判斷迴歸預測好壞的指標
MSE 平均平方誤差->越小越好
MAE 平均絕對誤差->越小越好
R-square決定係數 1以下，越接近1越好

介紹網站:https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/404042/
'''

#MAE
from sklearn.metrics import mean_absolute_error
MAE = mean_absolute_error(y_true,y_pred)

#MSE
from sklearn.metrics import mean_squared_error
MSE = mean_squared_error(y_true,y_pred)

#R-square
from sklearn.metrics import r2_score
R-square = 2_score(y, p(x))

