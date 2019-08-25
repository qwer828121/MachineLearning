'''
密度分群DBSCAN
參數須設定
eps:兩樣本被認為同群的最大距離 ->越大，群數越少
min_samples:被考慮為群中心的最小數目  ->越大，群數越少

詳細可以參考
https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html#sphx-glr-auto-examples-cluster-plot-dbscan-py

預測出來的數字為分群編號
0跟-1都不屬於任何一群
'''

from sklearn.cluster import DBSCAN
DBSCAN_cluster = DBSCAN(eps=3, min_samples=2)
X_cluster = DBSCAN_cluster.fit_predict(X)
