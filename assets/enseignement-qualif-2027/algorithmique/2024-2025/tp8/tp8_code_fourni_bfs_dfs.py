## Question 1

class SommetBFS(Sommet):
    
    def __init__(self, id, label):
        Sommet.__init__(self, id, label)
        # Initialisation de l'attribut couleur
        # Initialisation de l'attribut distance
        # Initialisation de l'attribut parent
        
## Question 4

def generer_graphe_aleatoire_bfs():
    G_aleat = Graphe()
    
    nb_sommets_min = 8
    nb_sommets_max = 15
    proba_creation_arete = 0.8
    
    nb_sommets_aleat = random.randint(nb_sommets_min, nb_sommets_max)
    
    for i in range(nb_sommets_aleat):
        G_aleat.ajout_sommet(SommetBFS)
    
    for i in range(nb_sommets_aleat):
        for j in range(nb_sommets_aleat):
            valeur_tiree = random.random()
            if valeur_tiree >= proba_creation_arete:
                G_aleat.ajout_arete(i, j)
    
    return G_aleat
    
## Question 7

def generer_graphe_aleatoire_dfs():
    G_aleat = Graphe()
    
    nb_sommets_min = 8
    nb_sommets_max = 15
    proba_creation_arete = 0.8
    
    nb_sommets_aleat = random.randint(nb_sommets_min, nb_sommets_max)
    
    for i in range(nb_sommets_aleat):
        G_aleat.ajout_sommet(SommetDFS)
    
    for i in range(nb_sommets_aleat):
        for j in range(nb_sommets_aleat):
            valeur_tiree = random.random()
            if valeur_tiree >= proba_creation_arete:
                G_aleat.ajout_arete(i, j)
    
    return G_aleat
