# Exercice 1

import math

def degres_en_radians(degres):
    radians = degres * math.pi / 180
    return radians

# Exercice 2

def compter_chiffre_dans_nombre(nombre, chiffre):
	compteur = 0
	for caractere in nombre:
		if caractere == str(chiffre):
			compteur += 1
	return compteur

# Exercice 3

def compter_tous_les_chiffres_dans_nombre(nombre):
    chiffres = [i for i in range(1, 10)]
    dict_occurrences = {}
    for chiffre in chiffres:
        dict_occurrences[chiffre] = compter_chiffre_dans_nombre(nombre, chiffre)

    return dict_occurrences

# Exercice 4

def inverser_chaine(chaine):
	i = len(chaine) - 1
	chaine_inversee = ""

	while i >= 0:
		chaine_inversee += chaine[i]
		i -= 1
	return chaine_inversee

# Exercice 5

def palindrome_numerique_taille_5():
    chiffres = [i for i in range(0, 10)]
    liste_palindromes = []

    for chiffre1 in chiffres:
        for chiffre2 in chiffres:
            for chiffre3 in chiffres:
                liste_palindromes.append(str(chiffre1) + str(chiffre2) + str(chiffre3) + str(chiffre2) + str(chiffre1))
    return liste_palindromes

# Exercice 6

def verification_palindrome(chaine):
    return chaine == inverser_chaine(chaine)

# Exercice 7

def sous_chaine(chaine, debut, fin):
    if 0 <= debut < len(chaine) and 0 <= fin < len(chaine) and debut < fin:
        return chaine[debut:fin+1]
    else:
        return "Indices invalides, impossible de générer la sous-chaîne."

# Exercice 8

def remplacement_caractere_dans_chaine(chaine, a_remplacer, remplacement):
    for i in range(len(chaine)):
        if chaine[i] == a_remplacer:
            chaine[i] = remplacement
    return chaine

# Exercice 9

def chaine_compressee(chaine):
    if len(chaine) == 0:
        return chaine

    chaine_compressee = ""
    compteur = 1

    for i in range(1, len(chaine)):
        if chaine[i] == chaine[i - 1]:
            compteur += 1
        else:
            chaine_compressee += chaine[i - 1] + str(compteur)
            compteur = 1

    chaine_compressee += chaine[-1] + str(compteur)

    return chaine_compressee

# Exercice 10

def pair_ou_impair(nombre):
    message = str(nombre) + " est un nombre impair."
    if nombre % 2 == 0:
        message = str(nombre) + " est un nombre pair."
    return message

# Exercice 11

def afficher_puissances_limite(base, valeur_somme_max):
    puissance = 0
    somme_puissances = 0
    chaine_a_afficher = ""

    while somme_puissances + base ** puissance <= valeur_somme_max:
        somme_puissances += base ** puissance
        chaine_a_afficher += str(base ** puissance) + " (" + str(base) + " ** " + str(puissance) + ") / "
        puissance += 1

    return chaine_a_afficher[:-2] # Permet de ne pas retourner le dernier " / "

# Exercice 12

def date_millionnaire(annee, taux, somme_depart):
    solde = somme_depart
    annee_actuelle = annee

    while solde < 1000000:
        solde *= taux
        annee_actuelle += 1

    return annee_actuelle

# Exercice 13 

def pyramide_de_chiffres():
    pyramide = ""
    for k in range(1, 10):
        pyramide += str(k) * k + "\n"
    return pyramide

# Exercice 14

def factorielle(n):  
    resultat = 1

    for i in range(1, n + 1):
        resultat *= i

    return resultat

# Exercice 15

def approximation_e_ordre_n(n):
    approximation_e = 0
    for i in range(n + 1):
        approximation_e += 1 / factorielle(i)

    return approximation_e

# Exercice 16

def maximum(liste_nombres):
    max_valeur = liste_nombres[0]

    for nombre in liste_nombres[1:]:
        if nombre > max_valeur:
            max_valeur = nombre

    return max_valeur

# Exercice 17

def minimum(liste_nombres):
    min_valeur = liste_nombres[0]

    for nombre in liste_nombres[1:]:
        if nombre < min_valeur:
            min_valeur = nombre

    return min_valeur

# Exercice 18

def est_premier(nombre):
    if nombre < 2:
        return False  # Les nombres inférieurs à 2 ne sont pas premiers

    diviseur = 2
    while diviseur * diviseur <= nombre:
        if nombre % diviseur == 0:
            return False  # Le nombre a un diviseur autre que 1 et lui-même
        diviseur += 1

    return True  # Le nombre est premier

# Exercice 19

def affichage_nombre_sauf_multiples(n, multiples_interdits):
	liste_a_retourner = []
	i = 1
	while i <= n:
		est_multiple_interdit = False

		for multiple in multiples_interdits:
			if i % multiple == 0:
				est_multiple_interdit = True
				break

		i += 1 
		if est_multiple_interdit:
			continue

		liste_a_retourner.append(i - 1)

	return liste_a_retourner

# Exerice 20 

def liste_est_vide(liste):
    return len(liste) == 0


# Exercice 21

def liste_est_vide_autrement(liste):
    return not liste

# Exercice 22

def acces_aleatoire(liste, indice):
    resultat = None
    if 0 <= indice < len(liste):
        resultat = liste[indice]
    return resultat

# La complexité temporelle asymptotique est en O(1) car l'accès aléatoire à une liste est en O(1) et l'accès à la longueur de la liste est en O(1) aussi.

# Exercice 23

def modifier_valeur(liste, indice, nouvelle_valeur):
    indice_valide = False
    if 0 <= indice < len(liste):
        liste[indice] = nouvelle_valeur
        indice_valide = True

    return liste, indice_valide

# La complexité temporelle asymptotique est en O(1) ici aussi, car l'accès aléatoire, l'affectation et l'accès à la longueur sont tous en O(1).

#Exercice 24

def ajouter_valeur_a_la_fin(liste, nouvelle_valeur):
    liste.append(nouvelle_valeur)
    return liste

# La complexité temporelle asymptotique de append() est en O(1).

# Exercice 25

def ajouter_valeurs_a_la_fin(liste, nouvelles_valeurs):
    liste.extend(nouvelles_valeurs)
    return liste

# La complexité temporelle asymptotique de cette fonction sera en O(k), où k est le nombre d'éléments à ajouter. En effet, l'ajout d'un élément est en O(1), et on répète cette opération k fois.

# Exercice 26

def longueur_liste(liste):
    return len(liste)

# La complexité temporelle asymptotique de len() est en O(1).

# Exercice 27

def longueur_liste_inefficace(liste):
    count = 0
    for element in liste:
        count += 1
    return count

# La complexité temporelle asymptotique est en O(n), étant donné que l'on parcourt les n éléments de la liste.

# Exercice 28

def liste_au_cube(liste):
    for i in range(len(liste)):
        liste[i] = liste[i] ** 3
    return liste

# Exercice 29

def liste_au_cube_comprehension(liste):
    return [x ** 3 for x in liste]

# Exercice 30 

def suppression_doublons(liste):
    liste_sans_doublons = []
    elements_vus = []

    for element in liste:
        if element not in elements_vus:
            elements_vus.append(element)
            liste_sans_doublons.append(element)
    return liste_sans_doublons

# Exercice 31

def rotation_droite_de_liste(liste, n):
    n_reel = n % len(liste)
    return liste[-n_reel:] + liste[:-n_reel] # Cette ligne fait intervenir la concaténation de deux listes et le "tranchage" (slicing) de liste. Par exemple, avec l'exemple de l'énoncé : n_rel vaut 2, dont on fait liste[-2:] + liste[:-2], soit la concaténation de liste[-2:] qui est la liste partant du deuxième élément en partant de la fin (soit [5, 6]) et liste[:-2] qui est la liste partant du début et s'arrêtant au deuxième élément en partant de la fin exclus (soit [1, 2, 3, 4]). On obtient bien [5, 6] + [1, 2, 3, 4] soit [5, 6, 1, 2, 3, 4].

# Exercice 32

# Les tuples sont non-modifiables, c'est à dire qu'une fois définis on ne peut changer leur valeur, alors que c'est possible pour les listes. 

# Exercice 33

def longueur_tuple(tup):
    return len(tup)

# La complexité temporelle asymptotique de len() est en O(1).

# Exercice 34

def indicage_tuples(liste_tuples):
    nouvelle_liste_tuples = []
    for i in range(len(liste_tuples)):
        nouvelle_liste_tuples.append((i, ) + liste_tuples[i])
    return nouvelle_liste_tuples

# Exercice 35

def min_et_max_tuples_taille_3(liste_tuples):
    somme_min = float('inf')
    position_min = 0
    somme_max = 0
    position_max = 0

    for i in range(len(liste_tuples)):
        somme = 0
        for element in liste_tuples[i]:
            somme += element

        if somme < somme_min:
            position_min = i
            somme_min = somme
        
        if somme > somme_max:
            position_max = i
            somme_max = somme

    return position_min, position_max


# Exercice 36

def tuple_trie_deuxieme_element(liste_tuples):
    def cle_tri(tup):
        return tup[1]

    liste_tuples.sort(key=cle_tri)
    return liste_tuples

# Cette façon de faire est assez directe et utilise une fonction de tri native sur les listes, où on peut spécifier la valeur sur laquelle se baser pour faire le tri.

# Exercice 37

# La principale différence est que les ensembles contiennent nécessairement des valeurs distinctes, et pas les listes. Les ensembles sont non-ordonnés par ailleurs, alors que les listes le sont.

# Exercice 38

def ajout_element_si_absent(ensemble, valeur):
    ensemble.add(valeur)
    return ensemble

# La complexité temporelle asymptotique de add() est en O(1).

# Exercice 39

def union_deux_ensembles(ensemble_1, ensemble_2):
    return ensemble_1.union(ensemble_2)

# La complexité temporelle asymptotique de union() est O(n_1 + n_2), avec n_1 et n_2 les tailles d'ensemble_1 et ensemble_2.

# Exercice 40

def intersection_deux_ensembles(ensemble_1, ensemble_2):
    return ensemble_1.intersection(ensemble_2)

# La complexité temporelle asymptotique de union() est O(n_1 + n_2), avec n_1 et n_2 les tailles d'ensemble_1 et ensemble_2.

# Exercice 41

def ensembles_disjoints(ensemble_1, ensemble_2):
    if len(ensembles_disjoints(ensemble_1, ensemble_2)) == 0:
        return True
    return False

# Exercice 42

# Les deux éléments que l'on retrouve pour chaque entrée dans un dictionnaire sont la clé et la valeur.

# Exercice 43

def remplacer_valeur_dictionnaire(dictionnaire, cle, nouvelle_valeur):
    dictionnaire[cle] = nouvelle_valeur
    return dictionnaire

# La complexité temporelle asymptotique est en O(1) car l'accès et l'affectation sur des dictionnaires sont en O(1).

# Exercice 44

def compter_occurrences_dans_liste(liste_elements):
    occurrences = {}
    for elem in liste_elements:
        if elem in occurrences:
            occurrences[elem] += 1 # Cas où elem a déjà été rencontré et est donc déjà dans le dictionnaire
        else:
            occurrences[elem] = 1 # Cas où l'on a jamais rencontré l'élément elem et donc qu'il n'est pas dans le dictionnaire
    return occurrences

# Exercice 45

def montant_total_ventes(ventes):
    montant_total = 0
    for vente in ventes:
        montant_total += vente['quantite_produit'] * vente['prix_unitaire']
    return montant_total

def produit_le_plus_vendu(ventes):
    max_quantite = 0
    nom_produit_associe = None

    for vente in ventes:
        if vente['quantite_produit'] > max_quantite:
            max_quantite = vente['quantite_produit']
            nom_produit_associe = vente['produit']
    return nom_produit_associe

def quantite_chaque_produit(ventes):
    result = {}
    for vente in ventes:
        produit = vente['produit']
        quantite = vente['quantite_produit']
        if produit in result:
            result[produit] += quantite
        else:
            result[produit] = quantite
    return result


# Exercice 46

# Représenter les coordonnées GPS d'une position sur une carte : Utiliser un tuple (latitude, longitude).
# Représenter une série de points dans le plan euclidien : Utiliser une liste de tuples [(x1, y1), (x2, y2), ...].
# Représenter plusieurs grandeurs physiques et leur dimension : Utiliser un dictionnaire {'masse':'kg', 'temps':'s', ...}.
# Représenter une classe d'étudiants avec, pour chacun d'entre eux, leur moyenne dans chaque matière : Utiliser un dictionnaire de dictionnaires {'nom_etudiant_1': {'math': 15, 'physique': 12, ...}, 'nom_etudiant_2': {'math': 18, 'physique': 14, ...}, ...}.
