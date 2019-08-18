'''
介紹幾個判斷分類預測好壞的指標
Accuracy 正確率->0~1之間 越大越好
Precision 準確率->0~1之間 越大越好
Recall 召回率-> 0~1之間 越大越好
F1 score -> 0~1之間 越大越好
ROC -> AUC 值 0~1之間 越大越好
介紹網站:https://www.ycc.idv.tw/confusion-matrix.html
'''

#cufussion matrix 混淆矩陣，下面4個值都是從這邊算出來的
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_true, y_pred)

#Accuracy正確率
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_true, y_pred)

#Precision準確率
from sklearn.metrics import precision_score
precision = precision_score(y_true, y_pred)

#Recall召回率
from sklearn.metrics import recall_score
recall = recall_score(y_true, y_pred)

#F1 score
from sklearn.metrics import f1_score
f1 = f1_score(y_true, y_pred) 

#ROC  (僅限二元分類)
#這邊的y_pred要是類似機率值的樣子，而不是直接預測的類別
#這樣才能透過不同門檻值，畫出ROC曲線
from sklearn.metrics import roc_curve, auc 
fpr,tpr,threshold = roc_curve(y_true, y_pred) 
roc_auc = auc(fpr,tpr) 


#補充 分類結果報告 
#https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html
from sklearn.metrics import classification_report
report = classification_report(y_true, y_pred, target_names=target_names)
report = classification_report(y_true, y_pred, labels=[1, 2, 3])
