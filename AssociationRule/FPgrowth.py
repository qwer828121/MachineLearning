'''
FP-growth
需先安裝套件pip install pyfpgrowth
英文版詳細使用說明https://medium.com/@pcm1312/implementing-fp-growth-in-python-170f3dc64d78

說明及大神代碼可參考
https://blog.csdn.net/songbinxu/article/details/80411388  
'''

#資料需要整理成transaction
import pyfpgrowth
patterns = pyfpgrowth.find_frequent_patterns(transactions, 2)  #2  最小支持度數量
rules = pyfpgrowth.generate_association_rules(patterns, 0.7)   #0.7 最小可信度

#輸出規則
print(rules)
