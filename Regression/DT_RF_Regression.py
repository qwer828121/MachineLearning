'''
決策樹DT(迴歸)
隨機森林RF
決策樹跟隨機森林都可以做迴歸或分類
這邊是迴歸的使用方式

參數部分共同的有
max_depth:最大深度
min_samples_split:最小分裂數量
random_state:隨機種子
'''

#決策樹訓練
from sklearn.tree import DecisionTreeRegressor
DT_regressor = DecisionTreeRegressor(random_state = 0)
DT_regressor.fit(X_train, Y)

#決策樹測試
y_pred = DT_regressor.predict(X_test)

#隨機森林訓練
#n_estimators: 用來設定決策樹數量
from sklearn.ensemble import RandomForestRegressor
RF_regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
RF_regressor.fit(X_train, Y)

#隨機森林測試
y_pred = RF_regressor.predict(X_test)
