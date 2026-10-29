'''
Correction de l'exercice 2 du TP2 d'algorithmique.
Utilisation du script : "/path_to_python/python3.exe /path_to_tp/correction_tp2_ex2.py element n" 
'''

import random
from tqdm import tqdm # La fonction "tqdm" permet de voir dans le terminal, la progression des itérations d'une boucle, et d'obtenir une estimation du temps restant avant 
import sys

def recherche_dichotomique_recursive(element, liste, position = 0):
    if len(liste) == 0:
        return -1

    m = len(liste) // 2

    if liste[m] == element:
        return position + m
    if liste[m] > element:
        return recherche_dichotomique_recursive(element, liste[:m], position)
    else:
        return recherche_dichotomique_recursive(element, liste[m+1:], position + m + 1) 

def main(arguments):

    print("\t Premier test : La liste vide.")

    liste = []
    element = arguments[1] # C'est l'argument "element" dans la description ci-haut

    recherche_dans_liste_vide = recherche_dichotomique_recursive(element, liste)
    print("La valeur retournée par l'algorithme dans le cas de la recherche de n'importe quel élément dans une liste vide est : " + str(recherche_dans_liste_vide) + ".\n")


    print("\t Deuxième test : Génération d'un très grand nombre de tests avec de l'aléatoire.")

    # Ce qui suit est un exemple de test automatisé, mais il existe de nombreuses façons de tester un programme.

    taille = int(arguments[2]) # C'est l'argument "n" dans la description ci-haut

    # On commence par créer une liste d'entiers qui prends aléatoirement les valeurs de [-taille, taille] avec une probabilité d'1/3 (valeur arbitraire).
    for i in range(-taille, taille):
        aleatoire = random.random()
        if aleatoire <= (1/3):
            liste.append(i)

    # On affiche la taille de la liste générée (ce nombre variera à chaque éxecution).
    print("Taille de la liste ordonnée avec des trous : " + str(len(liste)))


    # Pour chaque valeur dans [liste, liste], notre algorithme ne se trompe pas dans deux cas : soit il a déterminé que la valeur n'est pas dans la liste (-1) et effectivement la valeur n'y est pas, soit il a déterminé que la valeur est dedans, et la position donnée correspond à la position dans la liste.
    nb_errors = 0
    for i in tqdm(range(-taille, taille)): 
        recherche_element = recherche_dichotomique_recursive(i, liste)
        if (recherche_element == -1 and i not in liste) or (recherche_element != -1 and liste.index(i) == recherche_element):
            continue # Ce mot-clé permet d'indiquer au programme qu'on finit le tour de boucle ici, sans exécuter le code qui suit. Ainsi, une erreur sera ajoutée seulement si la condition n'est pas respectée.
        
        nb_errors += 1

    # On affiche le nombre d'erreurs réalisées par notre algorithme. Pour qu'il soit fonctionnel, on doit bien entendu observer 0.
    print("Nombre de valeurs pour lesquelles l'algorithme retourne le mauvais résultat : " + str(nb_errors))

if __name__ == "__main__":
    sys.exit(main(sys.argv))