# -*- coding: utf-8 -*-
"""
Created on Fri May 25 11:58:17 2018

@author: dell E5440
"""

import numpy as np
from values import *
from un import det
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
    nb_inversible = 0
    
    for n in range(int(math.pow(TOT_LETTER,m*m))):
        comb = combinaisons(list_letters, m*m, n)
        
        M=[]
        for x in range(m):
            M.append([])
            for y in range(m):
                M[x].append(comb[x*m+y])
            
        if(det(M)!=0 and isInversible(M)):
            nb_inversible += 1
            
    return nb_inversible
    
    
    

"""
Max de clé possible pour un code Hill 2x2
"""

