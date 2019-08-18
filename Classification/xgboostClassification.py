'''
xgboost
使用前請先安裝pip install xgboost
參數設定可參考https://blog.csdn.net/sb19931201/article/details/52557382

透過RamdonSearch找參數
可以參考https://www.kaggle.com/tilii7/hyperparameter-grid-search-with-xgboost
'''

#XG訓練
import xgboost as xgb
xg_classifier = xgboost.XGBClassifier(           
                 learning_rate=0.1,
                 max_depth=3,
                 min_child_weight=0.5,
                 n_estimators=100) 
                
xg_classifier.fit(X_train, Y)  

xg_classifier.booster().get_fscore().items()  #查看特徵重要性

#XG測試
xg_classifier.predict(X_test)

xg_classifier.predict_proba(X_test)  #預測機率值
