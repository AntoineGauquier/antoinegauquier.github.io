#### Contenu supplémentaire à utiliser pour le TP8.

### Fonction permettant de générer un digraphe (plus ou moins) aléatoire

import random

def generer_digraphe_aleatoire():
    G_aleat = Graphe()
    
    nb_sommets_min = 8
    nb_sommets_max = 12
    proba_creation_arete = 0.8
    
    nb_sommets_aleat = random.randint(nb_sommets_min, nb_sommets_max)
    
    for i in range(nb_sommets_aleat):
        G_aleat.ajout_sommet(SommetDFS)
    
    for i in range(nb_sommets_aleat):
        for j in range(nb_sommets_aleat):
            valeur_tiree = random.random()
            if valeur_tiree >= proba_creation_arete:
                aretes_a_creer = [False, False]
                valeur_tiree_choix_arete = random.random()

                # On fait le choix ici de n'ajouter qu'une arête par couple de sommets, pour des soucis de simplification d'implémentation. Dans un graphe "réellement aléatoire", il faudrait laisser la possibilité de créer deux arêtes par couple de sommet, avec une certaine probabilité.
                aretes_a_creer[0] = valeur_tiree_choix_arete >= 0.5
                aretes_a_creer[1] = not aretes_a_creer[0]
                
                G_aleat.ajout_arete_digraphe(i, j, aretes_a_creer[0], aretes_a_creer[1])
    
    return G_aleat