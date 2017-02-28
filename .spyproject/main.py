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
    l = 1
    F = makeF(F0,p0,l)
    print(F)
    elts = makeElements(EI,F0,w0,l,N)
    K = makeK(elts)
    print(K)
    w = calcW(K,F,w0,N)
    print(w)
    
if __name__ == '__main__':
    main()
    
