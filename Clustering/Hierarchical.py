'''
階層分群
不需要事先決定分群數量
先長出階層距離後，再決定分群數量

這邊的是AGNES聚類方式
'''

#畫出dendrogram來決定分群數量
import scipy.cluster.hierarchy as sch
dendrogram = sch.dendrogram(sch.linkage(X, method = 'ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distances')
plt.show()

#選擇分群數量因為組內距離小、組間距離大

#使用決定的分群數量來分群
from sklearn.cluster import AgglomerativeClustering
hierarchical_cluster = AgglomerativeClustering(n_clusters = 5, affinity = 'euclidean', linkage = 'ward')
X_cluster = hierarchical_cluster.fit_predict(X)
