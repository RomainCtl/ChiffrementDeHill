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
A=[[-1, 2, 5],
   [1, 2, 3],
   [-2, 8, 10]]
#print(gaussJordan(np.array(A)))

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
    """
    return l'inverse de a (int ou float) sur Z/x (mod x)
    """
    for i in range (1, x):
        if (a*i)%x == 1:
            return i
    return -1

def getInverse(m):
    """
    return l'inverse de la matrice m sur Z/TOT_LETTER (26)
    """
    d=det(m)
    m=gaussJordan(np.array(m))*d
    d1 = getInverseModX(d, TOT_LETTER)
    if d1 == -1: return None
    m=(m*d1)%TOT_LETTER
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

#print(crypteHill("ELECTION", [[9,4],[5,7]])) # = 'CTSIVVWF'
#print(dCrypteHill("CTSIVVWF", [[9,4],[5,7]])) # = 'ELECTION'

"""
t=crypteHill("ELECTION", [[1, 3, 3], [5, 3, 2], [7, 2, 5]])
print(t)
print(dCrypteHill(t, [[1, 3, 3], [5, 3, 2], [7, 2, 5]]))
"""


k=[[1, 3, 3],
   [5, 3, 2],
   [7, 2, 5]]
t=crypteHill("IL ETAIT UNE FOIS LHISTOIRE DUN ADO", k)
#print(t) # BDURHROZEJLERMRHRZHXTMZMHJKTFX
#print(dCrypteHill(t, k)) # ILETAITUNEFOISLHISTOIREDUNADOA


def getXfirstChar(st, m, args):
    """
    @param:
        st: list des chiffres correspondants a des lettre
        m: taille suppose de la matrice => la liste sera regroupe par m chiffres
        args: liste de m position des couples souhaite
    """
    N=[]
    for i in range(m):
        N.append([])
    for i in range(m):
        for j in range(m):
            #N[j].append(st[i*m+j])
            N[j].append(st[args[i]*m+j])
    return N

#TCL = [4,11,4,2,19,8,14,13]
#TCY = [2,19,18,8,21,21,22,5]
#k = [[9,4],[5,7]] => [[5, 12], [15, 25]]
TCL="ELECTION"
TCY="CTSIVVWF"
#print(getXfirstChar([4,11,4,2,19,8,14,13], 2))

#TCL="ILETAITUNEFOISLHISTOIREDUNADOA"
#TCY="BDURHROZEJLERMRHRZHXTMZMHJKTFX"

def CLRattak(tcy, tcl, m=2):
    """
    m taille suppose de la matrice
    prend en entrer un text cyrpte, et sa version decrypte
    return un tuple avec la clef de cryptage, et la liste des potentiels clef de cryptage trouve
    """
    res = []
    resOk = None
    tcy1=translateAlphaToInt(tcy)
    tcl1=translateAlphaToInt(tcl)
    if (len(tcy1)%m != 0): raise Exception("Warning ! len(tcy)%m != 0")
    while (len(tcl1)%m != 0):
        tcl.append(alphabet.A.value)

    if (len(tcy1) != len(tcl1)): raise Exception("Error ! le text crypté et decrypté ne font pas la meme taille !")
    
    isok=False
    
    ty = getInverse(getXfirstChar(tcy1, m, [0, 1]))
    tl = getXfirstChar(tcl1, m, [0, 1])
    
    while not isok:
        if ty != None:
            c = np.array(tl).dot(ty)
            k = getInverse(c%TOT_LETTER)
            if dCrypteHill(tcy, k) == tcl:
                resOk = k
                isok = True
            else:
                res.append(k)
        
        ty = getInverse(getXfirstChar(tcy1, m, [0, 2]))
        tl = getXfirstChar(tcl1, m, [0, 2])
        # TODO faire l'ago pour la liste de positions qui change a chaque passage

    #c = np.array(tl).dot(ty)
    #return getInverse(c%TOT_LETTER)
    return resOk, res

print(CLRattak(TCY, TCL))
g = np.array([[2, 19], [18, 8]])
p = gaussJordan(g)
#print(p)
#print(g.dot(p))
""" res =
[[  5.   3.   1.]
 [ 21.  14.  13.]
 [ 21.  11.   4.]]
"""

#st => chaine de caractère crypté
#k => 
def diagAttak(st, k, m=2):
    """
    m taille suppose de la matrice
    prend en entrer un text cyrpte
    return la clef de cryptage
    """
    pass
