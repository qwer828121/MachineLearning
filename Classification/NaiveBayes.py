'''
Naive Bayes單純貝氏分類器
二元跟多元分類 使用不同的function
'''

#二元單純貝氏分類器訓練
from sklearn.naive_bayes import GaussianNB
BayesClassifier = GaussianNB()
BayesClassifier.fit(X_train, y_train)

#二元單純貝氏分類器測試
y_pred = BayesClassifier.predict(X_test)


#多元單純貝氏分類器訓練
from sklearn.naive_bayes import MultinomialNB
BayesClassifier = MultinomialNB()
BayesClassifier.fit(X_train, y_train)

#多元單純貝氏分類器測試
y_pred = BayesClassifier.predict(X_test)
