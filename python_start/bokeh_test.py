# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 08:59:04 2021

@author: 18530
"""

from bokeh.plotting import figure, output_file, show, reset_output

import numpy as np

x=np.linspace(0,10,100)
y1=np.sin(x)
y2=np.cos(x)

# 出力設定
reset_output()

output_file("graph.html")

TOOLTIPS = [
    ("index", "$index"),
    ("(x,y)", "($x, $y)"),
]

# グラフ設定
p = figure(tooltips=TOOLTIPS, title="sin, cosカーブ", x_axis_label="x", y_axis_label="y")

# プロット
p.line(x, y1, legend="sin")
p.line(x, y2, legend="cos")

# 凡例をクリックしたときにプロットを非表示にする
p.legend.click_policy = "hide"

# グラフ表示
show(p)


