import matplotlib.pyplot as plt
from time import perf_counter
from tqdm import tqdm
import math

import sys
sys.setrecursionlimit(1000000)


# ---------- Exercice 1 ----------

print("---------- Exercice 1 ----------\n")

def suite_fibonacci_dynamique(n):
    valeurs_suite = [0]

    if n > 0:
        valeurs_suite.append(1)
    
    for i in range(2, n + 1):
        valeurs_suite.append(valeurs_suite[i - 1] + valeurs_suite[i - 2])

    return valeurs_suite[-1]

for i in range(21):
	print(suite_fibonacci_dynamique(i))


# ---------- Exercice 2 ----------

print("\n---------- Exercice 2 ----------\n")

def nombre_minimal_pieces_memoisation(P, S, k, structure_memoisation):
    key = (str(S), str(k))
    
    if key in structure_memoisation:
        return structure_memoisation[key]

    if S == 0:
        structure_memoisation[key] = 0
    elif (k == -1 and S >= 0) or S < 0:
        structure_memoisation[key] = math.inf
            
    else:
        structure_memoisation[key] = min(nombre_minimal_pieces_memoisation(P, S, k-1, structure_memoisation), 1 + nombre_minimal_pieces_memoisation(P, S - P[k], k, structure_memoisation))
    return structure_memoisation[key]


P_euro = [1, 2, 5, 10, 20, 50, 100, 200]
k = len(P_euro) - 1

print(nombre_minimal_pieces_memoisation(P_euro, 0, k, dict()))
print(nombre_minimal_pieces_memoisation(P_euro, 2, -1, dict()))
print(nombre_minimal_pieces_memoisation(P_euro, 1301, k, dict()))
print(nombre_minimal_pieces_memoisation(P_euro, 13, 2, dict()))
print(nombre_minimal_pieces_memoisation(P_euro, 113, 2, dict()))

# ---------- Exercice 3 ----------

print("\n---------- Exercice 3 ----------\n")

def nombre_minimal_pieces_memoisation_retour_structure(P, S, k, structure_memoisation):
    key = (str(S), str(k))
    
    if key in structure_memoisation:
        return key, structure_memoisation

    result = None
    if S == 0:
        structure_memoisation[key] = {'min_val':0, 'sous_struct':None}
    elif (k == -1 and S >= 0) or S < 0:
        structure_memoisation[key] = {'min_val':math.inf, 'sous_struct':None}
            
    else:
        left_key, left_memoisation = nombre_minimal_pieces_memoisation_retour_structure(P, S, k-1, structure_memoisation)
        right_key, right_memoisation = nombre_minimal_pieces_memoisation_retour_structure(P, S - P[k], k, structure_memoisation)
        
        min_key = None
        min_val = None
        if left_memoisation[left_key]['min_val'] < 1 + right_memoisation[right_key]['min_val']:
            min_key = left_key
            min_val = left_memoisation[left_key]['min_val']
        else:
            min_key = right_key
            min_val = 1 + right_memoisation[right_key]['min_val']

        structure_memoisation[key] = {'min_val':min_val, 'sous_struct':min_key}
    return key, structure_memoisation

def nombre_minimal_pieces_memoisation_avec_combinaison(P, S, k):
    combinaison = [-1 for i in range(k + 1)]
    key, memoisation = nombre_minimal_pieces_memoisation_retour_structure(P, S, k, dict())
    
    valeur_min = memoisation[key]['min_val']
    next_key = key

    while next_key is not None:
        indice_combinaison = int(next_key[1])
        combinaison[indice_combinaison] += 1
        next_key = memoisation[next_key]['sous_struct']
        
    return valeur_min, combinaison


valeurs_S = [1301, 113]
valeurs_k = [k, 2]

for idx in range(len(valeurs_S)):

    min_val, combinaison = nombre_minimal_pieces_memoisation_avec_combinaison(P_euro, valeurs_S[idx], valeurs_k[idx])
    print("Problème : rendre la monnaie sur " + str(valeurs_S[idx]) + " unités de monnaie avec un nombre minimal de pièces en utilisant le système monétaire " + str(P_euro[:valeurs_k[idx]+1]) + ".\n")
    print("Nombre minimal de pièces trouvé : " + str(min_val) + ", réparties comme suit.")
    for idx2 in range(valeurs_k[idx] + 1):
        if combinaison[idx2] == -1:
            print("*\tLa pièce ayant pour valeur " + str(P_euro[idx2]) + " n'est pas utilisée dans ce cas.")
        else:
            print("*\tLa pièce ayant pour valeur " + str(P_euro[idx2]) + " est utilisée " + str(combinaison[idx2]) + " fois.")
    print("\n")


