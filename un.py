# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
Projet Cryptographie :
Chiffrement de Hill

Romain, Simon, Kevin
"""

import numpy as np
import math
from values import *

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
    return pgcd(det(M), TOT_LETTER) == 1

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
    p = pgcd(d, TOT_LETTER)
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

def translateAlphaToInt(st):
    """
    tranforme une chaine de caractere en list de int
    """
    res=[]
    for e in range(len(st)):
        if st[e] != " ":
            res.append(alphabet[st[e]].value)
    return res

def getLetter(i):
    """
    return la lettre correspondant a un int
    """
    for c in alphabet:
        if c.value == i:
            return c.name
    return ""

def translateIntToAlpha(lst):
    """
    tranforme une list de int en chaine de caractere
    """
    res=""
    for e in range(len(lst)):
        res+=getLetter(lst[e])
    return res

#print(translateAlphaToInt("ABS DKD"))
#print(translateIntToAlpha([0, 1, 18, 3, 10, 3]))

def crypteHill(st, k):
    """
    Permet de crypter la chaine st avec la clef k
    """
    if not isInversible(k): raise Exception("Error ! invalid key !")

    res=[]
    m=len(k)
    c=translateAlphaToInt(st)
    while (len(c)%m != 0):
        c.append(alphabet.A.value)
    for e in range(int(len(c)/m)):
        for f in range(m):
            r=0
            for j in range(m):
                r+=k[f][j]*c[e*m+j]
            res.append(r%TOT_LETTER)
    return translateIntToAlpha(res)

def getInverseModX(a, x):
    for i in range (1, x):
        if (a*i)%x == 1:
            return i
    return -1

def getInverse(m):
    d=det(m)
    m=gaussJordan(np.array(m))*d
    m=(m*getInverseModX(d, TOT_LETTER))%TOT_LETTER
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = round(m[i][j])
    return m

def dCrypteHill(st, k):
    """
    Permet de decrypter la matrice st avec la clef k
    """
    if not isInversible(k): raise Exception("Error ! invalid key !")

    res=[]
    m=len(k)
    c=translateAlphaToInt(st)
    k=getInverse(k)
    for e in range(int(len(c)/m)):
        for f in range(m):
            r=0
            for j in range(m):
                r+=k[f][j]*c[e*m+j]
            res.append(r%TOT_LETTER)
    return translateIntToAlpha(res)

print(crypteHill("ELECTION", [[9,4],[5,7]])) # = 'CTSIVVWF'
print(dCrypteHill("CTSIVVWF", [[9,4],[5,7]])) # = 'ELECTION'

def getXfirstChar(st, m):
    N=[]
    for i in range(m):
        N.append([])
    for i in range(m):
        for j in range(m):
            N[j].append(st[i*m+j])
    return N

#TCL = [4,11,4,2,19,8,14,13]
#TCY = [2,19,18,8,21,21,22,5]
#k = [[9,4],[5,7]] => [[5, 12], [15, 25]]
TCL="ELECTION"
TCY="CTSIVVWF"
#print(getXfirstChar(TCL, 2))

def CLRattak(tcy, tcl, m=2):
    """
    m taille suppose de la matrice
    prend en entrer un text cyrpte, et sa version decrypte
    return la clef de cryptage
    """
    tcy=translateAlphaToInt(tcy)
    tcl=translateAlphaToInt(tcl)
    if (len(tcy)%m != 0): raise Exception("Warning ! len(tcy)%m != 0")
    while (len(tcl)%m != 0):
        tcl.append(alphabet.A.value)

    if (len(tcy) != len(tcl)): raise Exception("Error ! le text crypté et decrypté ne font pas la meme taille !")

    ty = getInverse(getXfirstChar(tcy, m))
    tl = getXfirstChar(tcl, m)
    print(tl)
    print(ty)

    c = np.array(tl).dot(np.array(ty))
    return getInverse(c%TOT_LETTER)

print(CLRattak(TCY, TCL))

def diagAttak(st, k, m=2):
    """
    m taille suppose de la matrice
    prend en entrer un text cyrpte
    return la clef de cryptage
    """
    pass
