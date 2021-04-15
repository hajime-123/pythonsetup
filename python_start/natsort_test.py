# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 16:53:19 2021

@author: 18530
"""
from natsort import natsorted

sample = ["a_12", "a_2", "a_0",  "a_10", "a_4"]
print(sorted(sample))
print(natsorted(sample, key=lambda y: y.lower()))


