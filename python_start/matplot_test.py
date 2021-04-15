# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 09:32:16 2021

@author: 18530
"""

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

