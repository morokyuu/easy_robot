# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 06:18:43 2023

@author: square
"""

import numpy as np
import matplotlib.pyplot as plt

def rotZ(th):
    return np.array([
        [ np.cos(th), np.sin(th), 0.0],
        [-np.sin(th), np.cos(th), 0.0],
        [          0,          0, 1.0]
        ])

def tr(x,y):
    return np.array([
        [        1.0,          0,   x],
        [          0,        1.0,   y],
        [          0,          0, 1.0]
        ])


l1 = 12
l2 = 8
l3 = 5

th1 = np.linspace(0, 1.57, 10)
th2 = 0.9
R01 = np.dot(rotZ(th1),tr(l1,0))
R12 = np.dot(rotZ(th2),tr(l2,0))

p0 = np.array([0,0,1])
p1 = np.dot(R01,p0)
p2 = np.dot(np.dot(R01,R12),p0)


fig,ax = plt.subplots(figsize = (5, 5))
ax.scatter(0,0)
ax.scatter(p1[0],p1[1])
ax.scatter(p2[0],p2[1])

# 軸ラベルの設定
ax.set_xlabel("x", fontsize = 16)
ax.set_ylabel("y", fontsize = 16)

# 軸範囲の設定
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)

ax.grid()


