'''
Correction du TP1 du cours d'Introduction à l'algorithmique du CPES CAD (2023 / 2024). 
L'exercice 4 sera corrigé lors de la séance de TP du 19/09.
Les exercices 5 et 6 ne seront pas corrigés en classe, mais une correction est présentée ici. 
Vous pouvez bien entendu modifier les valeurs définies pour changer les affichages obtenus.
'''

print('\n\t\t\t\tExercice 1\n')

print('\tExercice 1, question 1 : ')
print('(50-5*6+20)/4 = ' + str((50-5*6+20)/4) + '\n')

# Question 2

print('\tExercice 1, question 2 :')
print('Valeur décimale approchée par division : 17/3 = ' + str(round(17/3, 3)))
print('Que l\'on peut aussi retrouver par les opérateurs de division entière et de reste : 17//3 = ' + str(17//3) + ' et 17%3 = ' + str(17%3) + ', qui donne finalement : 17//3 + (17%3)/3 = ' + str(round(17//3 + (17%3)/3, 3)) + '\n')

# Question 3

print('\tExercice 1, question 3 : ')
print('Calcul de 2 puissance 5 avec l\'opérateur de puissance : 2 ** 5 = ' + str(2 ** 5))
print('Équivalent à une succession de multiplications : 2 * 2 * 2 * 2 * 2 = ' + str(2 * 2 * 2 * 2 * 2))


print('\n\n\t\t\t Exercice 2 \n')

# Question 1

print('\tExercice 2, question 1 : ')
print('Définition de trois variables floattantes : a = 1.6, b = 5.4 et c = 3.3')

a = 1.6
b = 5.4
c = 3.3

print('Vérification de leurs types : a est de type ' + str(type(a)) + ', b est de type ' + str(type(b)) + ' et c est de type ' + str(type(c)) + '.')
print('a < b ? ' + str(a < b))
print('a < c ? ' + str(a < c))
print('c < b ? ' + str(c < b))
print('Donc a < c < b. \n')

# Question 2

print('\tExercice 2, question 2 :')
a = 7
b = a - 4
print('a prend la valeur : ' + str(a) + ', b prend la valeur a - 4 = 7 - 4 = ' + str(b) +  ', et le produit a * b = ' + str(a) + ' * ' + str(b) + ' = ' + str(a*b) + '\n')

# Question 3

print('\tExercice 2, question 3 : ')
print('On commence par représenter les points A et B par deux paires de variables entières.')

Ax = 3
Ay = 4
Bx = 6
By = 8

print('On a donc : Ax = ' + str(Ax) + ', Ay = ' + str(Ay) + ', Bx = ' + str(Bx) + ' et By = ' + str(By) + '.')
print('On peut ensuite calculer leur distance euclidienne, et ce en faisant usage des opérateurs arithmétiques.')

distance =  ((Ax - Bx) ** 2 + (Ay - By) ** 2) ** 0.5

print('La formule est donc : ((Ax - Bx) ** 2 + (Ay - By) ** 2) ** 0.5 = ((' + str(Ax) + ' - ' + str(Bx) + ') ** 2 + (' + str(Ay) + ' - ' + str(By) + ') ** 2) ** 0.5 = ' + str(distance) + '\n')

# Question 4

print('\tExercice 2, question 4 : ')
print('On définit les variables du problème : les points C = (2, 2) et D = (4, 6) à l\'aide de deux paires de variables entières, et le rayon à l\'aide d\'une autre variable entière.')

Cx = 2
Cy = 2
Dx = 4
Dy = 6
rayon = 5

print('L\'équation cartésienne d\'un cercle est donnée par : (x - Cx) ** 2 + (y - Cy) ** 2 == rayon ** 2, soit (x - ' + str(Cx) + ') ** 2 + (y - ' + str(Cy) + ') ** 2 == ' + str(rayon) + ' ** 2 == ' + str(rayon ** 2) + '.')
print('Comme on souhaite savoir si D = (Dx, Dy) = (4, 6) est dans le cercle, on remplace (x, y) par (Dx, Dy). De plus, pour que le point soit inclus, il faut vérifier une inégalité et non une égalité via l\'opérateur inférieur ou égal : ')
print('(Dx - Cx) ** 2 + (Dy - Cy) ** 2 <= rayon ** 2, soit (' + str(Dx) + ' - ' + str(Cx) + ') ** 2 + (' + str(Dy) + ' - ' + str(Cy) + ') ** 2 <= ' + str(rayon ** 2) + '. On a alors : ' + str((Dx - Cx) ** 2 + (Dy - Cy) ** 2) + ' <= ' + str(rayon ** 2) + ' qui donne finalement : ' + str((Dx - Cx) ** 2 + (Dy - Cy) ** 2 <=  rayon ** 2) + '. Le point D est bien contenu dans le cercle de centre C et de rayon 5.')
print('Une solution plus directe proposée par plusieurs d\'entre vous consiste à simplement calculer la distance euclidienne entre C et D, et considérer que D est à l\'intérieur du cercle si et seulement si la distance est inférieure ou égale au rayon : ((Cx - Dx) ** 2 + (Cy - Dy) ** 2) ** 0.5 <= rayon, soit ((' + str(Cx) + ' - ' + str(Dx) + ') ** 2 + (' + str(Cy) + ' - ' + str(Dy) + ') ** 2) ** 0.5 <= ' + str(rayon) + ', qui donne ' + str(round(((Cx - Dx) ** 2 + (Cy - Dy) ** 2) ** 0.5, 3)) + ' <= ' + str(rayon)  + ', soit finalement : ' + str(((Cx - Dx) ** 2 + (Cy - Dy) ** 2) ** 0.5 <= rayon) + '.')


print('\n\n\t\t\tExercice 3\n')

# Question 1

print('\tExercice 3, question 1 : ')

resultat = 1

for i in range(5):
	resultat *= 2
	print('Le résultat à l\'itération ' + str(i + 1) + 'est : ' + str(resultat) + '.')

print('On retrouve donc bien le résultat obtenu à la question 3 de l\'exercice 1. \n')

# Question 2

print('\tExercice 3, question 2 : ')

print('On définit trois variables à virgules flottantes a, b et c.')

a = 3.14
b = 2.72
c = 1.62

if a < b and b < c and a < c:
	print('a (' + str(a) + ') < b (' + str(b) + ') < c (' + str(c) + ') \n')
elif a < b and c < b and a < c:
	print('a (' + str(a) + ') < c (' + str(c) + ') < b (' + str(b) + ') \n')
elif b < a and a < c and b < c:
	print('b (' + str(b) + ') < a (' + str(a) + ') < c (' + str(c) + ') \n')
elif b < c and c < a and b < a:
	print('b (' + str(b) + ') < c (' + str(c) + ') < a (' + str(a) + ') \n')
elif c < a and a < b and c < b:
	print('c (' + str(c) + ') < a (' + str(a) + ') < b (' + str(b) + ') \n')
else:
	print('c (' + str(c) + ') < b (' + str(b) + ') < a (' + str(a) + ') \n')

# Question 3

print('\tExercice 3, question 3 : ')
print('On commence par définir un entier de notre choix.')

nombre = 9

print('Ici, on a définit la variable entière nombre = ' + str(nombre) +  '.')

if nombre % 2 == 0:
	print('Comme nombre % 2 = ' + str(nombre) + ' % 2 = ' + str(nombre % 2) + ', alors le nombre est pair (car 2 est un de ses diviseurs). \n')
else:
	print('Comme nombre % 2 = ' + str(nombre) + ' % 2 = ' + str(nombre % 2) + ' > 0, alors le nombre est impair (car 2 n\'est pas un de ses diviseurs). \n')

# Question 4

print('\tExercice 3, question 4 : ')

resultat = 0
n = 1

while resultat < 12:
	resultat = n ** 2 - 4 * n
	print('Pour n = ' + str(n) + ' : resultat = ' + str(resultat) + '.')
	n += 1

print('Condition d\'arrêt atteinte, car resultat = ' + str(resultat) + '.')

print('\n\n\t\t\tExercice 4\n')

# Question 1

print('\tExercice 4, question 1 : ')

def distance_euclidienne(X1, X2, Y1, Y2):
	return ((X1 - Y1) ** 2 + (X2 - Y2) ** 2) ** 0.5

print('La distance euclidienne entre (3, 4) et (6, 8) est : ' + str(distance_euclidienne(3, 4, 6, 8)))
print('La distance euclidienne entre (12, 4) et (-22, 1) est : ' + str(round(distance_euclidienne(12, 4, -22, 1), 3)))
print('La distance euclidienne entre (7, -3) et (-5, -11) est : ' + str(round(distance_euclidienne(7, -3, -5, -11), 3)) + '\n')

def point_dans_cercle(centre1, centre2, rayon, point1, point2):
	return (point1 - centre1) ** 2 + (point2 - centre2) ** 2 <= rayon ** 2

print('Le point (4, 6) est-il inclus dans le cercle de centre (2, 2) et de rayon 5 ? ' + str(point_dans_cercle(2, 2, 5, 4, 6)))
print('Le point (6, 4) est-il inclus dans le cercle de centre (-1, 3) et de rayon 18 ? ' + str(point_dans_cercle(-1, 3, 18, 6, 4)))
print('Le point (-9, -3) est-il inclus dans le cercle de centre (-14, -2) et de rayon 3 ? ' + str(point_dans_cercle(-14, -2, -9, -3, 3)) + '\n')

# Question 2

print('\tExercice 4, question 2 : ')

def annee_bissextile(annee):
	return (annee % 4 == 0 and not annee % 100 == 0) or annee % 400 == 0

print('1900 est bissextile ? ' + str(annee_bissextile(1900)))
print('2000 est bissextile ? ' + str(annee_bissextile(2000)))
print('2018 est bissextile ? ' + str(annee_bissextile(2018)))
print('2022 est bissextile ? ' + str(annee_bissextile(2020)), '\n')

# Question 3

print('\tExercice 4, question 3 : ')

def table_multiplication(valeur):
	for index in range(10):
		print('\t' + str(index+1) + ' * ' + str(valeur) + ' = ' +  str((index + 1)*valeur))

print('Table de multiplications de 5 : ')
table_multiplication(5)
print('\n')

print('Table de multiplications de 13 : ')
table_multiplication(13)

# ---------- Fin des exercices corrigés en classe ----------

print('\n\n\t\t\tExercice 5 (Pour aller plus loin)\n')

# Question 1

print('\tExercice 5, question 1 : ')

def factorielle(n):
	if n == 0:
		return 1

	return n * factorielle(n-1)

print('Factorielle de 0 : ' + str(factorielle(0)))
print('Factorielle de 1 : ' + str(factorielle(1)))
print('Factorielle de 4 : ' + str(factorielle(4)))
print('Factorielle de 4 : ' + str(factorielle(6)))
print('Factorielle de 8 : ' + str(factorielle(8)) + '\n')

# Question 2

print('\tExercice 5, question 2 : ')

def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1

	return fibonacci(n-1) + fibonacci(n-2)

for idx in range(11):
	print('Fibonnaci de ' + str(idx) + ' : ' + str(fibonacci(idx)))
print('\n')

# Question 3

print('\tExercice 5, question 3 : ')

def livret_epargne(t, u0, n):
	if n == 0:
		return u0

	return t * livret_epargne(t, u0, n-1)

print('Considérons le cas u0 = 1500 et t = 1.05 (somme initiale de 1500€ sur le livret, avec un taux d\'intérêt de 5%). Voici l\'épargne du livret sur les 10 premières années : ')

t = 1.05
u0 = 1500

for index in range(11):
	print('Pour l\'année ' + str(index) + ', le montant sur le compte est de : ' +  str(round(livret_epargne(t, u0, index), 2)) + '€')

print('\n\n\t\t\tExercice 6 (Pour aller plus loin)\n')

print('Pour cet exercice, il faut manipuler les chaînes de caractères, et en particulier, exploiter l\'encodage des caractères. Il vous faut donc utiliser la table ASCII (dont une partie est présentée en slide 18 du cours du 12 septembre), afin de calculer les décalages de lettres dans le déchiffreur. \n')

def dechiffreur_de_cesar(message_chiffre):

	for decalage in range(1, 14):

		message_dechiffre = ""

		for lettre in message_chiffre:
			position_lettre = ord(lettre)

			if position_lettre >= 65 and position_lettre <= 90: # Cas des majuscules
				position_decalee = position_lettre - 65 - decalage

				if position_decalee < 0:
					position_decalee += 91
				else:
					position_decalee += 65

				message_dechiffre += chr(position_decalee)

			elif position_lettre >= 97 and position_lettre <= 122: # Cas des minuscules
				position_decalee = position_lettre - 97 - decalage

				if position_decalee < 0:
					position_decalee += 123
				else:
					position_decalee += 97

				message_dechiffre += chr(position_decalee)
			else: # Les autres caractères ne rentrent pas dans notre définition de l'alphabet
				print('L\'algorithme ne supporte que les messages cryptés en alphabet latin, ce qui n\'est pas le cas de \"' + str(message_chiffre) + '\"')
				return

		print('Décalage de ' + str(decalage) + ' du message crypté \"' + str(message_chiffre) + '\" donne : \"' + str(message_dechiffre) + '\"')
	print('\n')

dechiffreur_de_cesar('URYYB')
dechiffreur_de_cesar('uryyb')
dechiffreur_de_cesar('ZLWA')
dechiffreur_de_cesar('PAGLQ')
dechiffreur_de_cesar('SBWKRQ')
dechiffreur_de_cesar('LYNB')
dechiffreur_de_cesar('GRMUXOZNSOWAK')
dechiffreur_de_cesar('&é34(-è_çà)=')
