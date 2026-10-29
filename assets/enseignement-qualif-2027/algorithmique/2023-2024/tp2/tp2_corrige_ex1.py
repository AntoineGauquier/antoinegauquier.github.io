'''
Correction de l'exercice 1 du TP2 d'algorithmique.
Utilisation du script : "/path_to_python/python3.exe /path_to_tp/correction_tp2_ex2.py taille" 
'''

from random import random # Importe directement la fonction random de random. C'est équivalent à n'écrire que "import random", puis plus loin, d'utiliser "random.random()" (au lieu de juste "random()" comme décrit plus loin)
import math
import sys

def monte_carlo_pi(n):
	nb_points_dans_cercle = 0

	for i in range(n):
		x_genere = random()
		y_genere = random()

		if x_genere ** 2 + y_genere ** 2 <= 1:
			nb_points_dans_cercle += 1 # Pour rappel, a += 1 est équivalent à a = a + 1

	return 4*nb_points_dans_cercle/n

def estimation_ordre_de_grandeur():
	valeur_estimee = 0
	n = 1

	while abs(math.pi - valeur_estimee) > 10 ** (-3):
		n *= 10
		valeur_estimee = monte_carlo_pi(n)

	return n

def main(arguments):

	print("\tQuestion 2 : Test de la fonction pour plusieurs puissances de 10 pour n.")
	
	taille = int(arguments[1]) # C'est l'argument "taille" dans la description ci-haut

	for i in range(taille):
		print("La valeur estimée de Pi pour " + str(10 ** i) + " points générés est : " + str(round(monte_carlo_pi(10 ** i), 8)))

	print("\n\tQuestion 3 : Ordre de grandeur de n pour approcher Pi à 10 ** (-3).")

	n_estime = estimation_ordre_de_grandeur()

	print("L'ordre de grandeur de n pour approcher Pi à 10 ** (-3) est " + str(n_estime) + " (soit 10 ** " + str(math.log10(n_estime)) + "), donnant ici la valeur " + str(monte_carlo_pi(n_estime)) + ".")

if __name__ == "__main__":
    sys.exit(main(sys.argv))