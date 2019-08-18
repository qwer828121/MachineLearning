'''
SVM支持向量機
sklearn有支援多元分類，使用投票機制
另外SVM輸出為直接預測的label，不會是類似機率的數值

通常參數如下
kernel = linear’, ‘poly’, ‘rbf’, ‘sigmoid’
C: 懲罰項，越大越容易overfitting
'''

#SVM訓練
from sklearn.svm import SVC
SVMclassifier = SVC(kernel = 'rbf')
SVMclassifier.fit(X_train, y_train)

#SVM測試
y_pred = SVMclassifier.predict(X_test)
