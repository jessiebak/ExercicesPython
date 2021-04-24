# Enoncé : Dans une cours de récréation, 4 enfants qui ne savent pas vraiment compter essayent de savoir qui a le plus de carte pokémon. Ils savent combien ils en ont chacun, 
# mais il ne savent pas comparer les nombres entre eux, pour savoir dans l'ordre qui a le plus de carte pokémon, ensuite le deuxième, le troisième et enfin le dernier.
# SANS AUCUNE FONCTION AUTRE QUE PRINT ET INPUT (n'en créez pas non plus !) demandez à chacun des enfants 1 par 1 d'entrée leur nom et le nombre de carte qu'ils possèdent,
# Aucun des enfants n'a le même nombre de carte pokémon, ne traitez pas les égalités
# A la fin, le programme affichera quelque chose comme ceci :

# Entrez le prénom de la première personne :
# Sarah
# Entrez le nombre de cartes Pokémon que possède Sarah :
# 124
# Entrez le prénom de la deuxième personne :
# Rebecca
# Entrez le nombre de cartes Pokémon que possède Rebecca :
# 256
# Entrez le prénom de la troisième personne :
# Ismael
# Entrez le nombre de cartes Pokémon que possède Ismael :
# 55
# Entrez le prénom de la quatrième personne :
# Esau
# Entrez le nombre de cartes Pokémon que possède Esau :
# 273
# La personne avec le plus de cartes Pokémon est Esau avec 273 cartes Pokémon
# En deuxième vient Rebecca avec 256 cartes Pokémon
# En troisième position il y a Sarah avec 124 cartes Pokémon
# Enfin, en dernier il reste Ismael avec 55 cartes Pokémon


# Lorsque vous aurez fini ça, essayez de rajouter une 5 ème personne et le programme doit toujours fonctionner
# Enfin, lorsque tout ça marche, copiez collez votre programme dans un nouveau fichier Cette fois, les enfants peuvent avoir un nombre de carte identique,
# essayez de traiter les égalités du mieux que vous pouvez


#region indice
# Vos if peuvent s'imbriquer ! Un if peut se passer dans un if ou dans un else ou dans un elif !
#endregion

player1 = input("Entrez le nom de la première personne \t")
P1C= int(input(f"Quel est le nombre de carte de {player1}"))
player2 = input("Entrez le nom de la deuxième personne\t ")
P2C= int(input(f"Quel est le nombre de carte de {player2}"))
player3 = input("Entrez le nom de la troisième personne \t")
P3C= int(input(f"Quel est le nombre de carte de {player3}"))
player4 = input("Entrez le nom de la quatrième personne \t")
P4C= int(input(f"Quel est le nombre de carte de {player4}"))

 #TOUTES SOLUTIONS SI P1 EST PLUS GRAND
if P1C > P2C > P3C > P4C or P1C > P3C > P2C > P4C  or P1C > P4C > P3C > P2C or P1C > P4C > P2C > P3C or P1C > P3C > P4C > P2C or P1C > P2C > P4C > P3C:
	print(f"La première personne avec le plus de carte est {player1} avec {P1C}")
	if P2C > P3C > P4C or P2C > P4C > P3C :
		print(f"La deuxième personne avec le plus de carte est {player2} avec {P2C}")
		if P3C > P4C:
			print(f"La troisième personne avec le plus de carte est {player3} avec {P3C}")
			print(f"La quatrième personne avec le plus de carte est {player4} avec {P4C}")
		else: 
			print(f"La troisième personne avec le plus de carte est {player4} avec {P4C}")
			print(f"La quatrième personne avec le plus de carte est {player3} avec {P3C}")
	elif P3C > P2C > P4C or P3C > P4C > P2C :
		print(f"La deuxième personne avec le plus de carte est {player3} avec {P3C}")
		if P2C > P4C:
			print(f"La troisième personne avec le plus de carte est {player2} avec {P2C}")
			print(f"La quatrième personne avec le plus de carte est {player4} avec {P4C}")
		else: 
			print(f"La troisième personne avec le plus de carte est {player4} avec {P4C}")
			print(f"La quatrième personne avec le plus de carte est {player2} avec {P2C}")
	elif P4C > P2C > P3C or P4C > P3C > P2C :
		print(f"La deuxième personne avec le plus de carte est {player4} avec {P4C}")
		if P2C > P3C:
			print(f"La troisième personne avec le plus de carte est {player2} avec {P2C}")
			print(f"La quatrième personne avec le plus de carte est {player3} avec {P3C}")
		else: 
			print(f"La troisième personne avec le plus de carte est {player3} avec {P3C}")
			print(f"La quatrième personne avec le plus de carte est {player2} avec {P2C}")
	
	#TOUTES SOLUTIONS SI P1 EST PLUS GRAND 
elif P2C > P3C > P4C > P1C or P2C > P4C > P3C > P1C or P2C > P1C > P3C > P4C or  P2C > P1C > P4C > P3C or P2C > P3C > P1C > P4C or P2C > P4C > P1C > P3C :  
		print(f"La première personne avec le plus de carte est {player2} avec {P2C}")
		if P3C > P4C > P1C or P3C > P1C > P4C:
			print(f"La deuxième personne avec le plus de carte est {player3} avec {P3C}")
			if P4C > P1C: 
				print(f"La troisième personne avec le plus de carte est {player4} avec {P4C}")
				print(f"La quatrième personne avec le plus de carte est {player1} avec {P1C}")
			else : 
				print(f"La troisième personne avec le plus de carte est {player1} avec {P1C}")
				print(f"La quatrième personne avec le plus de carte est {player4} avec {P4C}")
		elif P4C > P1C > P3C or P4C > P3C > P1C :
			print(f"La deuxième personne avec le plus de carte est {player4} avec {P4C}")
			if P1C > P3C:
				print(f"La troisième personne avec le plus de carte est {player1} avec {P1C}")
				print(f"La quatrième personne avec le plus de carte est {player3} avec {P3C}")
			else: 
				print(f"La troisième personne avec le plus de carte est {player3} avec {P3C}")
				print(f"La quatrième personne avec le plus de carte est {player1} avec {P1C}")
		
		elif P1C > P4C > P3C or P1C > P3C > P4C :
			print(f"La deuxième personne avec le plus de carte est {player1} avec {P1C}")
			if P4C > P3C:
				print(f"La troisième personne avec le plus de carte est {player4} avec {P4C}")
				print(f"La quatrième personne avec le plus de carte est {player3} avec {P3C}")
			else: 
				print(f"La troisième personne avec le plus de carte est {player3} avec {P3C}")
				print(f"La quatrième personne avec le plus de carte est {player4} avec {P4C}")

	#TOUTES SOLUTIONS SI P3 EST PLUS GRAND
elif P3C > P2C > P4C > P1C or P3C > P4C > P2C > P1C or P3C > P1C > P2C > P4C or  P3C > P1C > P4C > P2C or P3C > P2C > P1C > P4C or P3C > P4C > P1C > P2C :  
		print(f"La première personne avec le plus de carte est {player3} avec {P3C}")
		if P2C > P4C > P1C or P2C > P1C > P4C:
			print(f"La deuxième personne avec le plus de carte est {player2} avec {P2C}")
			if P4C > P1C: 
				print(f"La troisième personne avec le plus de carte est {player4} avec {P4C}")
				print(f"La quatrième personne avec le plus de carte est {player1} avec {P1C}")
			else : 
				print(f"La troisième personne avec le plus de carte est {player1} avec {P1C}")
				print(f"La quatrième personne avec le plus de carte est {player4} avec {P4C}")
		elif P1C > P4C > P2C or P1C > P2C > P4C :
			print(f"La deuxième personne avec le plus de carte est {player1} avec {P1C}")
			if P4C > P2C:
				print(f"La troisième personne avec le plus de carte est {player4} avec {P4C}")
				print(f"La quatrième personne avec le plus de carte est {player2} avec {P2C}")
			else:
				print(f"La troisième personne avec le plus de carte est {player2} avec {P2C}")
				print(f"La quatrième personne avec le plus de carte est {player4} avec {P4C}")
		elif P4C > P1C > P2C or P4C > P2C > P1C :
			print(f"La deuxième personne avec le plus de carte est {player4} avec {P4C}")
			if P1C > P2C:
				print(f"La troisième personne avec le plus de carte est {player1} avec {P1C}")
				print(f"La quatrième personne avec le plus de carte est {player2} avec {P2C}")
			else: 
				print(f"La troisième personne avec le plus de carte est {player2} avec {P2C}")
				print(f"La quatrième personne avec le plus de carte est {player1} avec {P1C}")
		
		
elif P4C > P2C > P3C > P1C or P4C > P3C > P2C > P1C or P4C > P1C > P2C > P3C or  P4C > P1C > P3C > P2C or P4C > P2C > P1C > P3C or P4C > P3C > P1C > P2C :  
		print(f"La première personne avec le plus de carte est {player4} avec {P4C}")
		if P2C > P3C > P1C or P2C > P1C > P3C:
			print(f"La deuxième personne avec le plus de carte est {player2} avec {P2C}")
			if P3C > P1C: 
				print(f"La troisième personne avec le plus de carte est {player3} avec {P3C}")
				print(f"La quatrième personne avec le plus de carte est {player1} avec {P1C}")
			else : 
				print(f"La troisième personne avec le plus de carte est {player1} avec {P1C}")
				print(f"La quatrième personne avec le plus de carte est {player3} avec {P3C}")
		elif P1C > P3C > P2C or P1C > P2C > P3C :
			print(f"La deuxième personne avec le plus de carte est {player1} avec {P1C}")
			if P3C > P2C:
				print(f"La troisième personne avec le plus de carte est {player3} avec {P3C}")
				print(f"La quatrième personne avec le plus de carte est {player2} avec {P2C}")
			else:
				print(f"La troisième personne avec le plus de carte est {player2} avec {P2C}")
				print(f"La quatrième personne avec le plus de carte est {player3} avec {P3C}")
		elif P3C > P1C > P2C or P3C > P2C > P1C :
			print(f"La deuxième personne avec le plus de carte est {player3} avec {P3C}")
			if P1C > P2C:
				print(f"La troisième personne avec le plus de carte est {player1} avec {P1C}")
				print(f"La quatrième personne avec le plus de carte est {player2} avec {P2C}")
			else: 
				print(f"La troisième personne avec le plus de carte est {player2} avec {P2C}")
				print(f"La quatrième personne avec le plus de carte est {player1} avec {P1C}")
		
		