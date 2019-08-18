'''
決策樹DT(分類)
隨機森林RF
決策樹跟隨機森林都可以做迴歸或分類
這邊是分類的使用方式
參數部分共同的有
criterion :標準 可選擇"gini" or "entropy"
max_depth:最大深度
min_samples_split:最小分裂數量
random_state:隨機種子
'''

#決策樹訓練
from sklearn.tree import DecisionTreeClassifier
DT_classifier = DecisionTreeClassifier(criterion = 'entropy')
DT_classifier.fit(X_train, y_train)

#決策樹測試
y_pred = DT_classifier.predict(X_test)

#隨機森林訓練
#n_estimators: 用來設定決策樹數量
from sklearn.ensemble import RandomForestClassifier
RF_classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy')
RF_classifier.fit(X_train, y_train)

#隨機森林測試
y_pred = RF_classifier.predict(X_test)
