當資料沒有標籤(label)  
此時無法做迴歸及分類  
但是可以針對資料的X分布狀況進行分群  
有以下四種類型  
(前三種大致說明可以看這裡 https://ithelp.ithome.com.tw/articles/10193760)  
(或是這裡 https://allanhsu83117.github.io/2018/09/clustering-with-R/)  
(或是這裡https://zhuanlan.zhihu.com/p/37856153)  
  
1.分區分群(Partitioning)  
--代表:Kmeans、Kmedoids  
2.階層分群(Hierarchical)  
--代表:AGNES、DIANA  
3.密度分群(Density Based)  
--代表:DBSCAN  
4.模型分群(Model Based)  
--代表:SOM
  
另外判斷分群好壞的指標Evaluate  
  
**如果想使用非常詳細分群套件  
**可以參考pyclustering https://pypi.org/project/pyclustering/  
