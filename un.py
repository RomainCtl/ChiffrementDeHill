# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
Projet Cryptographie :
Chiffrement de Hill

Romain, Simon, Kevin
"""

import numpy as np

def pgcd(a, b):
    """
    return le plus grand diviser commun entre a et b
    """
    g = (a if a>b else b)
    p = (a if a<b else b)
    r = -1
    while r != 0:
        r = g%p
        if r==0: break
        g = p
        p = r
        if g == p: break
    return abs(p)

def det2x2(M):
    """
    return la determinant d'un matrice 2x2
    """
    return M[0][0]*M[1][1]-M[0][1]*M[1][0]

def det(M):
    """
    return la determinant d'un matrice carre nxn
    """
    if (len(M) == 0): raise Exception("Error ! la matrice est vide !")
    if (len(M) != len(M[0])): raise Exception("Error ! la matrice n'est pas une matrice carré !")

    if (len(M) == 2):
        return det2x2(M)
    else:
        N=[]
        for i in range(len(M)-1):
            N.append([])
            for j in range(len(M)-1):
                N[i].append(det2x2([
                    [M[i][j],
                     M[i][j+1]],
                    [M[i+1][j],
                     M[i+1][j+1]]]))
        return det(N)

def isInversible(M):
    """
    return true si une matrice est inversible
    false sinon
    """
    return pgcd(det(M), 26) == 1

def gaussJordan(M):
    """
    return la matrice inverse de M
    """
    (n,p)=M.shape
    A=np.concatenate((M,np.eye(n)),axis=1)
    for c in range(0,n):
        if A[c,c]!=0 :
            A[c]=A[c]/A[c,c]
        else :
            pivot=0
            while A[pivot,c]==0:
                pivot=pivot+1
            A[c]=A[c]+A[pivot]/A[pivot,c]
        for l in range(0,n):
            if c!=l :
                A[l]=A[l]-A[l,c]*A[c]
    return A[:,n:(2*n)]

"""
A = [[-2, 2, -3],
     [-1, 1, 3],
     [2, 0, -1]]
# res = 18
print(det(A))

B= [[-1, 2],[-3, 4]]
# res = 2
print(det(B))
"""

def calcAndDisplay(M):
    """
    Permet de calculer et d'afficher le pgcd du det
    """
    d = det(M)
    p = pgcd(d, 26)
    print(M)
    print("determinant : ", d)
    print("pgcd : ", p)
    if p == 1: print("Cette matrice est inversible sur Z/26")
    print('-----------------')

"""
# Question 1
B = [[2, 3],
     [7, 5]]
calcAndDisplay(B)

# Question 2
C = [[1, 3, 2], [5, 3, 2], [7, 2, 5]]
calcAndDisplay(C)

D = [[1, 3, 3], [5, 3, 2], [7, 2, 5]]
calcAndDisplay(D)

# Question 3
"""
def crypteHill(st, k):
    """
    Permet de crypter la matrice st avec la clef k
    """
    pass

def dCrypteHill(st, k):
    """
    Permet de decrypter la matrice st avec la clef k
    """
    pass

def CLRattak(tcy, tcl, m=2):
    """
    m taille suppose de la matrice
    prend en entrer un text cyrpte, et sa version decrypte
    return la clef de cryptage
    """
    pass

# sur 10 000
TOT_FREQ = 10000
freqApp = {
    "ES": 305,
    "LE": 246,
    "EN": 242,
    "DE": 215,
    "RE": 209,
    "NT": 197,
    "ON": 164,
    "ER": 163,
    "TE": 163,
    "SE": 155,
    "ET": 143,
    "QU": 134,
    "NE": 127,
    "OU": 118,
    "AI": 117,
    "EM": 113,
    "IT": 112,
    "ME": 104,
    "IS": 103,
    "LA": 101,
    "EC": 100,
    "TI": 98,
    "CE": 98,
    "ED": 96,
    "IE": 94,
    "RA": 92,
    "IN": 90,
    "EU": 89,
    "UR": 88,
    "CO": 87,
    "AR": 86,
    "TR": 86,
    "UE": 85,
    "TA": 85,
    "EP": 82,
    "ND": 80,
    "NS": 79,
    "PA": 78,
    "US": 76,
    "SA": 75,
    "SS": 73,
    "AN": 30
}

def diagAttak(st, k, m=2):
    """
    m taille suppose de la matrice
    prend en entrer un text cyrpte
    return la clef de cryptage
    """
    pass
