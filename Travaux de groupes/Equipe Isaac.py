print("Bonjour, Bienvenue dans notre parc d'attraction. \n Veuillez entrer les informations suivantes: ")
age = int(input("Age: "))
sexe = input("Sexe ( h ou f ): ")
nationalite = input("Nationalité : ")
taille = int(input("Taille (en cm ): "))
poids = float(input("Poids : "))
poils= input("Avez-vous des poils sur le corps ? (oui ou non)")
signesastro= int(input("Veuillez entrer le chiffre qui correspond à votre signe astrologique:\n 1 - Belier\n2 - Taureau\n3 - Gémeaux\n4 - Cancer\n5 - Lion\n6 - Vierge\n7 - Balance\n8 - Scorpion\n9 - Sagittaire\n10 - Capricorne\n11 - Verseau\n12 - Poisson\n"))


def Attractions(_age, _signeastro, _sexe, _taille, _nationalite, _poids, _poils):
	print ("Vous pouvez effectuer les attractions suivantes: ")
	if((_age >= 18 and ( _signeastro == 4 or _signeastro == 7 or _signeastro == 12)) or (_sexe == "f" and _taille >= 160) or (_age >= 45)): 
		print("- Grand Splash")
	if((_nationalite =="allemand")or (_sexe =="f" and _taille >= 150) or (_signeastro == 10 )):
		print(" - Rivière sauvage")
	if((_sexe=="f" and _age<=18 and _taille<= 130 and _poids <= 45) or (_sexe=="h" and _signeastro == 3) ):
		print ("- Grand 8")
	if((_nationalite=="japonais" or _nationalite=="allemand" or _nationalite=="italien") and (_age>=89 and _age<=120 and _sexe == "h") and (_nationalite=="autrichien" or _age<= 17) or (_sexe =="f" and _age>=25 and _age<=35)):
		print("-autotemponeuse")
	if((_taille<=140 and _age>=18) or (_sexe=="h")):
		print("-Caroussel")
	if((_sexe=="f" and _age>=45 ) or _taille<=150):
		print("- Chaise volante.")
	if((_age>=25 and _sexe=="h" and _taille>=180 and _poids>=80 and (_signeastro==5 or _signeastro==9)) or (_sexe=="f")):
		print(" Trampoline. ")
	if((_nationalite=="nigeria" and _age>=14) or (_taille>=150)):
		print("- Chenille")
	if (_sexe == "h" and _poils =="oui" and _taille > 140 and poids > 30 and (_signeastro ==4 or _signeastro==10 or _signeastro == 11)) or (_sexe== "f" or _poils=="oui" and _age <60 and (_signeastro == 7 or _signeastro == 12)) or (_age < 14 and _signeastro ==4) or (_nationalite == "Marocain" and _age < 70):
		print(" - Loup-Garou")
	
	
Attractions(age, signesastro, sexe, taille, nationalite, poids, poils)