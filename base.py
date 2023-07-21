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


v1 = np.array([[10,0,1.0],[0,10,1.0],[10,10,1.0]]).T

th = 0.3
vd1 = np.dot(v1[:,0],rotZ(th))
vd2 = np.dot(v1[:,1],rotZ(th))
vd3 = np.dot(v1[:,2],rotZ(th))


fig,ax = plt.subplots(figsize = (5, 5))

ax.scatter(v1[0],v1[1])
ax.scatter(vd1[0],vd1[1])
ax.scatter(vd2[0],vd2[1])
ax.scatter(vd3[0],vd3[1])

# 軸ラベルの設定
ax.set_xlabel("x", fontsize = 16)
ax.set_ylabel("y", fontsize = 16)

# 軸範囲の設定
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)

ax.grid()


