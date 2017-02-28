
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 21:11:11 2017

@author: hiroya
"""

import numpy as np
from Element import *

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

def makeK(elts):
    tmpK = []
    for elt in elts:
        tmpK.append(elt.makeKbCblist())
    return mergeMatrix(tmpK,len(elts))
    
def makeElements(EI,F,w0,l,N):
    elts = []
    for i in range(N):
        elts.append(Element(EI,F,w0,l,N))
    print(elts)
    #K1 = elt.makeKbCblist()
    return elts   
    
def calcW(K,F,w0,N):
    list = checknotfixedNum(w0)
    num = len(list)
    tmpf = []
    for i in list:
        tmpf.append(F[i])
    f = np.array(tmpf)
            
    Mat = [[0 for i in range(num)] for j in range(num)]
    for i in range(num):
        for j in range(num):
            Mat[i][j] = K[list[i]][list[j]]
    
    print(Mat)
    invMat = np.linalg.inv(Mat)
    tmpw = invMat.dot(f)
    w = np.zeros(2*N+2)
    for i in range(len(tmpw)):
        w[list[i]] = tmpw[i]
    return w
    
def checknotfixedNum(w):
    num = []
    for i in range(len(w)):
        if not w[i] == 0:
            num.append(i)
    return num

def makeF(F0,p0,l):
    num = len(F0)
    p = np.zeros(num)
    for i in range(num):
        if i % 2 == 0:
            p[i] = 2
    p[0] = 1
    p[-2] = 1
    p = -p*l/(num-2)*p0
    return p+F0
        
    
    
    
    
    
    
    
    
    
def hello():
    print("test")
         