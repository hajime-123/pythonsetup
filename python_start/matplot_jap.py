# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 12:06:04 2021

@author: 18530
"""

from numpy.random import *
from matplotlib import pyplot as plt

# 乱数生成
rand_nums = randn(100)

# 追加部分 フォントを指定する。
#plt.rcParams["font.family"] = "IPAexGothic"
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']

# ヒストグラム表示
plt.hist(rand_nums)
plt.xlabel("X軸と表示したい")
plt.ylabel("Y軸と表示したい")

