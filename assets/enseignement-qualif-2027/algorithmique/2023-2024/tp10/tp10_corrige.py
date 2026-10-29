#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

def gauche(i):
    return 2*i+1

def droite(i):
    return 2*i+2

def entasser_min(A, i):
    l = gauche(i)
    r = droite(i)
    
    if l < len(A) and A[l] < A[i]:
        min = l
    else:
        min = i

    if r < len(A) and A[r] < A[min]:
        min = r

    if min != i:
        A[i], A[min] = A[min], A[i]
        A = entasser_min(A, min)
    return A

def construction_tas_min(A):
    for i in range(math.floor(len(A)/2) - 1, -1, -1):
        A = entasser_min(A, i)
    return A


# In[2]:


A = [16, 14, 10, 9, 8, 7, 4, 3, 2, 1]
print(A)
tas_min_A = construction_tas_min(A)
print(tas_min_A)


# In[3]:


def entasser_min_partiel(A, i, n):
    l = gauche(i)
    r = droite(i)
    
    if l < n and A[l] < A[i]:
        min = l
    else:
        min = i

    if r < n and A[r] < A[min]:
        min = r

    if min != i:
        A[i], A[min] = A[min], A[i]
        A = entasser_min_partiel(A, min, n)
    return A

def tri_par_tas(A):
    A = construction_tas_min(A)
    print(A)
    print("==========================================")
    for i in range(len(A) - 1, -1, -1):
        print(A)
        A[0], A[i] = A[i], A[0]
        print(A)
        A = entasser_min_partiel(A, 0, i)
        print(A)
        print("-------------------------------------")
    print("==========================================")
    return A


# In[4]:


A = [16, 14, 10, 9, 8, 7, 4, 3, 2, 1]
print(tri_par_tas(A))


# On se retrouve avec la liste A initiale ... C'est normal, elle était déjà triée par ordre décroissant !
