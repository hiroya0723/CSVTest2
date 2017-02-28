# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 21:07:30 2017

@author: hiroya
"""

import numpy as np
from Element import *
import matplotlib.pyplot as plt
import time
from calcMethods import * 

def main():
    N=4
    w0 = np.array([0,0,1,1,1,1,1,1,1,1])
    F0 = np.array([0,0,0,0,0,0,0,0,0,0])
    p0 = 4.0
    EI=1
    l = 1.0
    F = makeF(F0,p0,l)
    print(F)
    hello()
    elts = makeElements(EI,F0,w0,l,N)
    K = makeK(elts)
    M = makeM(elts)
    print(M)
    print(K)
    w = calcW(K,F,w0,N)
    showGraph(w,l,l*N+l)
    
if __name__ == '__main__':
    main()
    
