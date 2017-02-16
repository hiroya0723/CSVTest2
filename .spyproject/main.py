# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 21:07:30 2017

@author: hiroya
"""

import numpy as np
from Element import *
import matplotlib.pyplot as plt
import time

def mergeMatrix(Mat,N):
    num = 2*N+2
    tmpMat = [[0 for i in range(num)] for j in range(num)]
    i=0    
    for mat in Mat:
        for y in range(4):
            for x in range(4):
                tmpMat[i*2+y][i*2+x] += mat[y][x]
        i = i+1     
    return tmpMat
    
def calcW(K,F,w,N):
    list = checknotfixedNum(w)
    num = len(list)
    tmpf = []
    for i in list:
        tmpf.append(F[i])
    f = np.array(tmpf)
            
    Mat = [[0 for i in range(num)] for j in range(num)]
    for i in range(num):
        for j in range(num):
            Mat[i][j] = K[list[i]][list[j]]
    invMat = np.linalg.inv(Mat)
    return invMat.dot(f)    
    
def checknotfixedNum(w):
    num = []
    for i in range(len(w)):
        if not w[i] == 0:
            num.append(i)
    return num
         
def main():
    N=1
    w0 = np.array([0,0,1,1])
    F0 = np.array([0,0,98,0])
    EI=100
    l = 1
    elt = Element(EI,F0,w0,l,N)
    K1 = elt.makeKbCblist()
    elt2 = Element(EI,F0,w0,l,N)
    K2 = elt.makeKbCblist()
    elt3 = Element(EI,F0,w0,l,N)
    K3 = elt.makeKbCblist()
    elts = [K1]
    K = mergeMatrix(elts,N)
    w = (calcW(K,F0,w0,N))
    print(w)
    
if __name__ == '__main__':
    main()
    
