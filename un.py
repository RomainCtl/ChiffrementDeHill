# -*- coding: utf-8 -*-
#!/usr/bin/env pyhton3

"""
Projet Cryptographie :
Chiffrement de Hill

Romain, Simon, Kevin
"""

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
    d = det(M)
    p = pgcd(d, 26)
    print(M)
    print("determinant : ", d)
    print("pgcd : ", p)
    if p == 1: print("Cette matrice est inversible sur Z/26")
    print('-----------------')

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




