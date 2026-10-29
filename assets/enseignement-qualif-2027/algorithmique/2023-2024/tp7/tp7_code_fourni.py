#### Contenu supplémentaire à utiliser pour le TP7.

### Méthodes supplémentaires de la classe Graphe

class Graphe:
    ...
    
    def __str__(self):
        if self.n == 0:
            return "Le graphe est vide."
        
        resultat = "Le graphe est composé des sommets :\n"
        
        for id in self.sommets:
            s = self.sommets[id]
            resultat += "-\tNuméro " + str(s.id)
            if s.label != "":
                resultat += "(label: " + s.label + ")"
            resultat += ", ayant pour voisin(s) le(s) sommet(s) numéro(s) : " + str(s.voisins) + "\n"
        resultat += "Au total, " + str(self.n) + " sommets et " + str(self.m) + " arêtes."
        return resultat
    
    def __getitem__(self, id):
        return self.sommets[id]

### Début de l'implémentation de la classe SommetBFS, héritante de la classe Sommet

class SommetBFS(Sommet):
    
    def __init__(self, id, label):
        Sommet.__init__(self, id, label)
        # Initialisation de l'attribut couleur
        # Initialisation de l'attribut distance
        # Initialisation de l'attribut parent

### Fonction permettant de générer un graphe (plus ou moins) aléatoire

import random

def generer_graphe_aleatoire():
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