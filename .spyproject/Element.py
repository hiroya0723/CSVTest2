# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 22:13:04 2017

@author: hiroya
"""

import numpy as np

class Element(object):  
    def __init__(self,EI,F0,w0,l,N):
        self.EI = EI    
        self.F0 = F0
        self.w0 = w0
        self.l = l
        self.N = N
        
    def makeKblist(self):
        l = self.l
        tmp = [[0 for i in range(4)] for j in range(4)]
        i = 0
        j = 0
        tmp[i][j] = 12.0/l**3
        j = j + 1
        tmp[i][j] = -6.0/l**2
        j = j + 1
        tmp[i][j] = -12/l**3
        j = j + 1
        tmp[i][j] = -6/l**2
        i = i + 1
        j = 0
        tmp[i][j] = -6/l**2
        j = j + 1
        tmp[i][j] = 4/l
        j = j + 1
        tmp[i][j] = 6/l**2
        j = j + 1
        tmp[i][j] = 2/l
        i = i + 1
        j = 0
        tmp[i][j] = -12/l**3
        j = j + 1
        tmp[i][j] = 6/l**2
        j = j + 1
        tmp[i][j] = 12/l**3
        j = j + 1
        tmp[i][j] = 6/l**2
        i = i + 1
        j = 0
        tmp[i][j] = -6/l**2
        j = j + 1
        tmp[i][j] = 2/l
        j = j + 1
        tmp[i][j] = 6/l**2
        j = j + 1
        tmp[i][j] = 4/l

       # w = self.w
       # i = 0
        #for  in w:
        #    print(f)
        
        return np.array(tmp)*self.EI

    def makeMblist(self):
        l = self.l
        tmp = [[0 for i in range(4)] for j in range(4)]
        i = 0
        j = 0
        tmp[i][j] = 156
        j = j + 1
        tmp[i][j] = -22*l
        j = j + 1
        tmp[i][j] = 54
        j = j + 1
        tmp[i][j] = 13*l
        i = i + 1
        j = 0
        tmp[i][j] = -22*l
        j = j + 1
        tmp[i][j] = 4*l**2
        j = j + 1
        tmp[i][j] = -13*l
        j = j + 1
        tmp[i][j] = -3*l**2
        i = i + 1
        j = 0
        tmp[i][j] = 54
        j = j + 1
        tmp[i][j] = -13*l
        j = j + 1
        tmp[i][j] = 156
        j = j + 1
        tmp[i][j] = 22*l
        i = i + 1
        j = 0
        tmp[i][j] = 13*l
        j = j + 1
        tmp[i][j] = -3*l**2
        j = j + 1
        tmp[i][j] = 22*l
        j = j + 1
        tmp[i][j] = 4*l**2

        return tmp      
        
    def checknotfixedNum(self):
        num = []
        for i in range(len(self.w0)):
            if not self.w0[i] == 0:
                num.append(i)
        return num
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        