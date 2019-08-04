'''
逐步回歸
逐步挑選特徵

向前選取 Forward
向後選取 Backward
雙邊選取

python內並無現成套件可以使用
網上有人透過statsmodels.formula.api寫出

向前選取 https://planspace.org/20150423-forward_selection_with_statsmodels/
雙邊選取 https://datascience.stackexchange.com/questions/24405/how-to-do-stepwise-regression-using-sklearn/24447#24447
向後選取如下
'''

import statsmodels.api as sm
def backwardElimination(X,Y, stop_p):
    X = sm.add_constant(X)
    numVars = len(X.columns)
    #numVars = len(x[0])
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(Y, X).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)
        if maxVar > stop_p:
            re_col = regressor_OLS.pvalues[regressor_OLS.pvalues==maxVar].index
            X=X.drop(re_col.tolist(), axis=1)
            '''
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    x = np.delete(x, j, 1)
            '''        
    regressor_OLS.summary()
    return X
    
    stop_p = 0.05 #自行設定p_value
    backwardElimination(X,Y, stop_p)
