'''
K 鄰近鄰居法
本身演算法不需要訓練
但使用Sklearn套件，會須先生成一些資訊，可參考以下
https://stats.stackexchange.com/questions/349842/why-do-we-need-to-fit-a-k-nearest-neighbors-classifier

所以還是必須先fit
另外KNN 建議可以先標準化X
n_neighbors 可以調整
'''

#建議可以先標準化X，可以參考DataPreprocessing/ScaleTransform.py
from sklearn.preprocessing import StandardScaler
st_scalar  = StandardScaler()
X_train = st_scalar .fit_transform(X_train)
X_test = st_scalar .transform(X_test)

#KNN 訓練(再次強調，本身演算法不需要訓練，但Sklearn需生成一些資訊)
from sklearn.neighbors import KNeighborsClassifier
KNNClassifier = KNeighborsClassifier(n_neighbors = 5)
KNNClassifier.fit(X_train, y_train)

# KNN預測
y_pred = classifier.predict(X_test)
