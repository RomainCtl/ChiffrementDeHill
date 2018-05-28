# -*- coding: utf-8 -*-
"""
Created on Fri May 25 11:58:17 2018

@author: dell E5440
"""

import numpy as np
from values import *
from un import *
import itertools
import math


def combinaisons(l, size, n):
    combinaison = []
    
    for x in range(size):
        combinaison.append(l[int(n/math.pow(len(l), x)%len(l))])
        
    return combinaison


"""
Programme de comptage du nombre de clés possibles 
en fonction de la taille de la matrice
"""

def nb_cle_hill(m=2):
    
    list_letters = range(TOT_LETTER)
    
    combinations = list(itertools.combinations(list_letters, m*m))
    
    for l in combinations:
        M = []
        for x in range(m):
            M = M+[]
            for y in range(m):
                M[x] = M[x]+[l[m*x+y]]
        print(M)
    
    
    

"""
Max de clé possible pour un code Hill 2x2
"""

