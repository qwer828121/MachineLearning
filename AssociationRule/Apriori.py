'''
Apriori演算法
使用前請務必安裝pip install apyori
https://pypi.org/project/apyori/
參數可調
min_support : 最小支持度 
min_confidence : 最小可信度
min_lift :最小作用度  (>1 才有效)
min_length : 最小數量
'''

#如果原本資料已整理成dataframe，請先串接成transaction
#dataset:原本的dataframe
#length_data:資料筆數
#max_item:最多的品項數量
transactions = []
for i in range(0, length_data):
    transactions.append([str(dataset.values[i,j]) for j in range(0, max_item)])

#apriori演算法
from apyori import apriori
rules = apriori(transactions, min_support = 0.001, min_confidence = 0.2, min_lift = 3, min_length = 2)

#results存放找尋出來的規則
results = list(rules)

#查看規則 可自行調整編號
print(results[0])
