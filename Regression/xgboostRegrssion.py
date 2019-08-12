'''
xgboost
使用前請先安裝pip install xgboost
參數設定可參考https://blog.csdn.net/sb19931201/article/details/52557382
'''

#XG訓練
import xgboost as xgb
xg_regression = xgboost.XGBRegressor(           
                 learning_rate=0.1,
                 max_depth=3,
                 min_child_weight=0.5,
                 n_estimators=100) 
                
xg_regression.fit(X_train, Y)  

xg_regression.booster().get_fscore().items()  #查看特徵重要性

#XG測試
xg_regression.predict(X_test)
