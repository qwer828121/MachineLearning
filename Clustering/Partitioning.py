'''
分區分群
代表Kmeans、Kmedoids
需事先決定分群數量n_clusters
下面代表Kmeans
'''

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 5, init = 'k-means++')
X_cluster = kmeans.fit_predict(X)


'''
分群數量決定
可以使用Elbow Method
嘗試不同的分群數量，找轉折處當分群數
http://rpubs.com/skydome20/R-Note9-Clustering
'''

k_test = 20              #嘗試1~20群
distance_k = []          #儲存每群內距離
for i in range(1, k_test):   
    kmeans = KMeans(n_clusters = i, init = 'k-means++'2)
    kmeans.fit(X)
    distance_k.append(kmeans.inertia_)
    
plt.plot(range(1, k_test), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('Distance_k')
plt.show()               #轉折處為選擇的分群數量
