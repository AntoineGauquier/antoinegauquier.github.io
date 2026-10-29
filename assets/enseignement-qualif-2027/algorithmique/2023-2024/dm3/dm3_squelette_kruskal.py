def algorithme_kruskal(graphe):
    A = [] # Liste des objets AreteKruskal à retourner une fois l'ACPM calculé
    
    # Création d'une liste d'objets Ensemble (un objet par sommet dans graphe)

    aretes = []
    for sommet in graphe.sommets: # On utilise la liste d'adjacence pour créer notre liste d'arêtes "AreteKruskal"
        for voisin in graphe[sommet].voisins:
            aretes.append(AreteMST(sommet, voisin['id'], voisin['poids']))

    aretes.sort(key =lambda arete:arete.poids) # On trie la liste de toutes les arêtes par ordre croissant de poids (fait appel aux lambdas Python)
    
    # Reste de l'algorithme Kruskal ... Devant faire appel aux fonctions d'Union-Find.
    
    return A
