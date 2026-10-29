'''
Correction de l'exercice 3 du TP2 d'algorithmique.
Utilisation du script : "/path_to_python/python3.exe /path_to_tp/correction_tp2_ex3.py" 
'''

import sys

def algo_euclide_recursif(a, b):
	if b == 0:
		return a
	
	return algo_euclide_recursif(b, a % b) 

def algo_euclide_iteratif(a, b):
	while b != 0:
		r = a % b
		a = b
		b = r
	
	return a
	

def main(arguments): # Ici aucun argument n'est utilisé. 

	print("\tQuestion 2 : Vérifier avec quelques paires d'entiers.")

	paires = [(126, 297), (1231, 754), (26187, 11223)]

	for paire in paires:
		print("Le résultat du PGCD entre " + str(paire[0]) + " et " + str(paire[1]) + " est : " + str(algo_euclide_recursif(paire[0], paire[1])) + ".")


if __name__ == "__main__":
    sys.exit(main(sys.argv))
