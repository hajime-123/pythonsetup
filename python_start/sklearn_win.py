# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 10:49:19 2021

@author: 18530
"""

import pandas as pd

wine = pd.read_csv("winequality-red.csv", sep=";")
#print(wine.head)

# sklearn.linear_model.LinearRegression クラスを読み込み
from sklearn import linear_model
clf = linear_model.LinearRegression()
 
# 説明変数に "density (濃度)" を利用
X = wine.loc[:, ['density']]
 
# 目的変数に "alcohol (アルコール度数)" を利用
Y = wine['alcohol']
 
# 予測モデルを作成
clf.fit(X, Y)
 
# 回帰係数
print(clf.coef_)
 
# 切片 (誤差)
print(clf.intercept_)
 
# 決定係数
print(clf.score(X, Y))





