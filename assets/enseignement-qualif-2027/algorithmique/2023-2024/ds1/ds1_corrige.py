#!/usr/bin/env python

def clef_plus_grande_valeur(d):
    plus_grande_valeur = None
    resultat = None

    for clef in d:
        if plus_grande_valeur == None or plus_grande_valeur<d[clef]:
            plus_grande_valeur=d[clef]
            resultat=clef

    return resultat

def mot_plus_frequent(l):
    occurrences = {}
    for mot in l:
        if mot in occurrences:
            occurrences[mot] += 1
        else:
            occurrences[mot] = 1
    return clef_plus_grande_valeur(occurrences)

def enumere_mots(s):
    for m in s.split():
        m = m.strip(";,.?!«»*…-–—[]'’”‘‘").lower()
        if m != "":
            yield m

with open("ile_mysterieuse.txt") as f:
    print(mot_plus_frequent(enumere_mots(f.read())))

class Chaine:
    def __init__(self, chaine):
        self.__c=chaine

    def taille(self):
        return len(self.__c)

    def est_bien_parenthesee(self):
        pile = []
        correspondance={"[": "]", "(": ")"}
        for c in self.__c:
            if c in correspondance:
                pile.append(c)
            else:
                if len(pile)>0 and correspondance[pile[len(pile)-1]]==c:
                    pile.pop()
                else:
                    return False
        return len(pile)==0

c = Chaine("(([])[()])[]")
print(c.taille())
print(c.est_bien_parenthesee())
c = Chaine("(([])[()][]")
print(c.taille())
print(c.est_bien_parenthesee())
