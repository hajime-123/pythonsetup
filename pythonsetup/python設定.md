

## １pythonの設定を行う

windowsインストーラ64ビットを選択

![Test Image 1](python設定画像\1.PNG)

pathはDドライブにする

インストールの方法はカスタムを選択する

![1](python設定画像\2.PNG)



![1](python設定画像\3.PNG)

install for all userにチェック

保存場所変更

![1](python設定画像\4.PNG)



![1](python設定画像\5.PNG)

試しにpythonを実行してみる

hello_test.py作成

![1](python設定画像\6.PNG)

実行してみた

![1](python設定画像\7.PNG)

次にpipを試してみた

pandasインストールして実行できるか確認

![1](python設定画像\8.PNG)



pandas_test.py

```
import pandas as pd

d = {
    'a': [1, 2, 3],
    'b': [5, 6, 7],
}
data_b = pd.DataFrame(d)

```

![1](python設定画像\11.PNG)

spyderも入れてみた

```
pip install spyder
```

以下のコマンドで起動

```
spyder
```

ただエラーが出ている

![1](python設定画像\10.PNG)

下記を入れたほうがいいの？

```
pip install spyder-kernels==2.0.1
```

requirements.txtをファイルに出力する。

```
pip freeze > requirements.txt
```

`requirements.txt`を別の環境にコピーして一括インストールする。

```
 pip install -r requirements.txt
```

bokehも入れてみた

```
pip install bokeh==0.13.0
```

```
import bokeh
bokeh.__version__
```

bokeht_test.py

```python
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

```

matplotlibも入れてみた

```
pip install matplotlib
```

matplot_test.py

```python
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,10,100)
y1=np.sin(x)
y2=np.cos(x)

fig, ax = plt.subplots()
ax.plot(x,y1, label="sin")
ax.plot(x,y2, label="cos")
ax.legend()
plt.show()
```



natsortを入れてみる

```
pip install natsort
```

natsort_test.py

```python
from natsort import natsorted

sample = ["a_12", "a_2", "a_0",  "a_10", "a_4"]
print(sorted(sample))
print(natsorted(sample, key=lambda y: y.lower()))
```

flaskを入れてみる

```
pip install Flask==1.1.2
```

flask_test.py

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    name = "Hello World"
    return name

@app.route('/good')
def good():
    name = "Good"
    return name

## おまじない
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000,threaded=True)
```

scikit-learnを入れてみる

```bash
pip install scikit-learn
```

https://pythondatascience.plavox.info/scikit-learn/%E7%B7%9A%E5%BD%A2%E5%9B%9E%E5%B8%B0

以上を参考にする

http://archive.ics.uci.edu/ml/datasets/Wine+Quality

[winequality-red.csv]をダウンロード

![1](python設定画像\12.PNG)

sklearn_win.py

```python
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
```

![1](python設定画像\13.PNG)

opencv入れてみる

```
pip install opencv-python
```

opencv_test.py

```python
import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while( cap.isOpened() ):

    ret, frame = cap.read()
    cv2.imshow('Capture',frame)
    key = cv2.waitKey(1)
    #print( '%08X' % (key&0xFFFFFFFF) )
    if key & 0x00FF  == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
```

cv2.CAP_DSHOWを入れると動作が遅くなるらしい？

tkinterはあらかじめ入っているみたい

tkinter_test.py

```python
import tkinter

root = tkinter.Tk()
root.title(u"Software Title")
root.geometry("400x300")

#ラベル
Static1 = tkinter.Label(text=u'test')
Static1.pack()

root.mainloop()
```

matplotlibの日本語化に関して

matplot_jap.py

```python
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

```



## ２pathの確認

パスが通っているか確認

pythonとScriptsのパスが通っていたらpython実行環境、ライブラリ実行環境がある

![1](python設定画像\9.PNG)