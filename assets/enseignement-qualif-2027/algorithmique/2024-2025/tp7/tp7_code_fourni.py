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