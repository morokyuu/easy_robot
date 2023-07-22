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

def drawLine(ax, xy0, xy1, color="green"):
    v = np.vstack((xy0[:2],xy1[:2])).T
    ax.plot(v[0],v[1], color=color)




def robot(lp,th):
    R01 = np.dot(rotZ(th[0]),tr(lp[0,0],lp[0,1]))
    R12 = np.dot(rotZ(th[1]),tr(lp[1,0],lp[1,1]))
    R23 = np.dot(rotZ(th[2]),tr(lp[2,0],lp[2,1]))
    
    p0 = np.array([0,0,1])
    p1 = np.dot(R01,p0)
    p2 = np.dot(np.dot(R01,R12),p0)
    p3 = np.dot(np.dot(np.dot(R01,R12),R23),p0)
    
    fig,ax = plt.subplots(figsize = (5, 5))
    ax.scatter(0,0)
    ax.scatter(p1[0],p1[1])
    ax.scatter(p2[0],p2[1])
    ax.scatter(p3[0],p3[1])
    # link
    drawLine(ax, p0, p1)
    drawLine(ax, p1, p2)
    drawLine(ax, p2, p3)
    # 軸ラベルの設定
    ax.set_xlabel("x", fontsize = 16)
    ax.set_ylabel("y", fontsize = 16)
    # 軸範囲の設定
    ax.set_xlim(-30, 30)
    ax.set_ylim(-30, 30)
    ax.grid()


lp = np.array([
    [12,0,1.0],
    [ 8,0,1.0],
    [ 5,0,1.0]
    ])
th = np.array([0.3,0.1,0.0])

robot(lp,th)



