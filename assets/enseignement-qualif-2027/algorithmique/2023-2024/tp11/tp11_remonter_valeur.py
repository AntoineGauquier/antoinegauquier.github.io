 def remonter_valeur(A, valeur):
    '''
    Cette fonction permet de remonter un sommet dans la file de priorité lorsque l'attribut distance de ce dernier est modifié.
    A est un Tas-Min représenté par une liste Python contenant des objets SommetDijkstra,
    valeur est l'objet SommetDijkstra à remonter dans la file de priorité.
    '''
    idx_valeur = A.index(valeur)
    while i >= 0 and A[idx_valeur] < A[idx_valeur // 2]:
        tmp = A[idx_valeur]
        A[idx_valeur] = A[idx_valeur // 2]
        A[idx_valeur // 2] = tmp 

        idx_valeur = idx_valeur // 2
    return A
