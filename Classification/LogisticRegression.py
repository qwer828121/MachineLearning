'''
邏輯迴歸
邏輯迴歸是一個二元分類器
如果要做多元分類,記得設定參數如下
multi_class='multinomial'
也可以加入懲罰項
penalty : ‘l1’, ‘l2’, ‘elasticnet’ or ‘none’, optional (default=’l2’)
'''

#邏輯迴歸訓練
from sklearn.linear_model import LogisticRegression
LogisticRegression = LogisticRegression()  #要做多元分類，要加multi_class='multinomial'
LogisticRegression.fit(X_train, y_train)

# 邏輯迴歸預測
y_pred = LogisticRegression.predict(X_test)
