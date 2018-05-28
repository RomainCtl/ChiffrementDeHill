# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
Projet Cryptographie :
Chiffrement de Hill

Romain, Simon, Kevin
"""

import numpy as np
import math
import itertools
import collections
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

def delspace(st):
    """
    @return:
        le string st sans espace
    """
    tmp = st.split(" ")
    return "".join(tmp)

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
    return l'inverse de a (int ou float) sur Z/x (mod x) (ou -1 si pas d'inverse)
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

def dCrypteHill(st, k, reverseKey=True):
    """
    Permet de decrypter la matrice st avec la clef k
    """
    if reverseKey and not isInversible(k): raise Exception("Error ! invalid key !")

    res=[]
    m=len(k)
    c=translateAlphaToInt(st)
    if reverseKey: k=getInverse(k)
    for e in range(int(len(c)/m)):
        for f in range(m):
            r=0
            for j in range(m):
                r+=k[f][j]*c[e*m+j]
            res.append(r%TOT_LETTER)
    return translateIntToAlpha(res)

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
            N[j].append(st[args[i]*m+j])
    return N

#TCL = [4,11,4,2,19,8,14,13]
#TCY = [2,19,18,8,21,21,22,5]
#k = [[9,4],[5,7]] => [[5, 12], [15, 25]]
#TCL="ELECTION"
#TCY="CTSIVVWF"

TCL="ILETAITUNEFOISLHISTOIREDUNADOA"
TCY="BDURHROZEJLERMRHRZHXTMZMHJKTFX"

def CLRattak(tcy, tcl, m=2):
    """
    m taille suppose de la matrice
    prend en entrer un text cyrpte, et sa version decrypte
    return un tuple:
        - la clef de cryptage
        - la clef de decryptage
        - liste de toutes les autres clefs de cryptage trouve
        - liste de toutes les autres clefs de decryptage trouve
    """
    tcy = delspace(tcy)
    tcl = delspace(tcl)
    cryptRes = []
    dcryptRes = []
    cryptResOk = None
    dcryptResOk = None
    tcy1=translateAlphaToInt(tcy)
    tcl1=translateAlphaToInt(tcl)
    if (len(tcy1)%m != 0): raise Exception("Warning ! len(tcy)%m != 0")
    while (len(tcl1)%m != 0):
        tcl.append(alphabet.A.value)

    if (len(tcy1) != len(tcl1)): raise Exception("Error ! le text crypté et decrypté ne font pas la meme taille !")

    # creation de la liste de toutes les possibilite de combinaison des positions
    li=range(int(len(tcy)/m))
    possibility = list(itertools.combinations(li, m))

    # cherche la clef
    ty = getInverse(getXfirstChar(tcy1, m, possibility[0]))
    tl = getXfirstChar(tcl1, m, possibility[0])

    for i in range(1, len(possibility)):
        if ty is not None:
            c = np.array(tl).dot(ty)%TOT_LETTER
            k = getInverse(c)
            if k is not None:
                if dCrypteHill(tcy, k) == tcl:
                    cryptResOk = k
                    dcryptResOk = c
                    break
                else:
                    cryptRes.append(k)
            else:
                if dCrypteHill(tcy, c, False) == tcl:
                    dcryptResOk = c
                    break
                else:
                    dcryptRes.append(c)
        
        ty = getInverse(getXfirstChar(tcy1, m, possibility[i]))
        tl = getXfirstChar(tcl1, m, possibility[i])

    return cryptResOk, dcryptResOk, cryptRes, dcryptRes

print(CLRattak(TCY, TCL, 3))
""" res =
[[  5.   3.   1.]
 [ 21.  14.  13.]
 [ 21.  11.   4.]]
"""


k = [[9,4],[5,7]]
TCL = "BONJOUR JE SUIS UN ETUDIANT EN INFORMATIQUE ET JESSAYE DE DECRYPTE CE CODE"
#"BO NJ OU RJ ES UI SU NE TU DI AN TE NI NF OR MA TI QU EE TJ ES SA YE DE DE CR YP TE CE CO DE"
#"NZ XY YC HS EQ EA IW DP RB HT AN FT TR HW MH EI VV QM AW ZC EQ GM YS RR RR IZ QR FT IM WE RR"
TCY = crypteHill(TCL, k)
print(TCY)
#print(CLRattak(TCY, TCL))

def maxCount(liste):
    maxi = {'count': 0}
    n=-1
    for i in range(len(liste)):
        if liste[i]['count'] > maxi['count']:
            maxi = liste[i]
            n=i
    return maxi, n

def combinaisons(l, size, n):
    """
    @param:
        l: list des element
        size: taille de la combinaison
        n: position de la combinaison
    """
    combinaison = []
    for x in range(size):
        combinaison.append(l[int(n/math.pow(len(l), x)%len(l))])
    return combinaison

#st => chaine de caractère crypté
def diagAttak(st, m=2):
    """
    @param:
        m : int, taille suppose de la matrice
        st: string, texte crypte
    @return:
        la clef de cryptage ou de decryptage
    """
    ty=translateAlphaToInt(st)
    # regroupe par m les lettres
    reg=[]
    for i in range(int(len(ty)/m)):
        tmp=[]
        for j in range(m):
            tmp.append(ty[i*m+j])
        reg.append(tuple(tmp))
    
    #cherche les tuples en double ou plus
    res=[{'tuple': i, 'count': c} for i, c in collections.Counter(reg).items()]
    res.sort(key= lambda i: i['count'], reverse=True)
    
    if res != []:
        # on trie la liste par order decroissant
        nres=[res[e]['tuple'] for e in range(len(res))]
        del res
        nres = list(itertools.combinations(nres, m))
        
        #
        freq = [list(freqApp)[i].name for i in range(len(freqApp))]
        possibility = list(itertools.combinations(freq, m))
        for j in range(len(nres)):
            tcy=""
            for p in range(m):
                tcy += translateIntToAlpha(nres[j][p])
    
            r=[]
            for i in range(len(possibility)):
                tcl = "".join(possibility[i])
                crykey, dcrykey, cryl, dcryl = CLRattak(tcy, tcl)
                if crykey is not None or dcrykey is not None:
                    print(tcl, tcy)
                    print(i, crykey, dcrykey, cryl, dcryl)
                    break
                elif cryl != [] or dcryl != []:
                    print(tcl, tcy)
                    print(i, cryl, dcryl)
                    break
        
    else:
        # 
        pass
    return None


print(diagAttak(TCY))


