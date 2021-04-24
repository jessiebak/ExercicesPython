print("Bienvenue dans notre magnifique parc! Voici quelques informations à remplir afin de connaitre les attractions qui vous sont accessibles:")
age= int(input("Entrez votre âge: "))
sexe= input("Entre votre sexe (M-F-X): ")
natio= input("Entrez votre nationalité: ")
taille= int(input("Entre votre taille (cm): "))
poids= int(input("Entrez votre poids (kg): "))
signe= int(input("1 - Bélier \n 2 - Taureau \n 3 - Gémeaux \n 4 - Cancer \n 5 - Lion \n 6 - Vierge \n 7 - Balance \n 8 - Scorpion \n 9 - Sagitaire \n 10 - Capricorne \n 11 - Verseau \n 12 - Poisson \n Choissisez votre signe astrologique :"))
import sys
if signe>12:
    sys.exit("Ce signe n'existe pas.")
if sexe !="H" and sexe !="F" and sexe !="X":
    sys.exit("Ce sexe n'existe pas.")
    
def splash(_age,_signe,_sexe,_taille):
	ok= "Grand Splash : Accessible."
	refus= "Grand Splash : Accès refusé."
	if _age>18 and (_signe==5 or _signe==8 or _signe==12):
		_reponse=ok
	elif _sexe=="F" and _taille>160:
		_reponse=ok
	elif _age>45:
		_reponse=ok
	else:
		_reponse=refus
	return _reponse

def riviere(_natio, _sexe, _age, _taille, _signe):
	ok= "Rivière Sauvage : Accessible."
	refus= "Rivière Sauvage : Accès refusé."
	if _natio== "Allemand":
		_reponse=ok
	elif _sexe== "F" and _taille>150 and _age==12:
		_reponse=ok
	elif _signe==10:
		_reponse=ok
	else:
		_reponse=refus
	return _reponse

def grandhuit(_sexe,_age,_taille,_poids,_signe):
	ok= "Grand Huit : Accessible."
	refus= "Grand Huit : Accès refusé."
	if _sexe=="F" and _age<10 and _taille<130 and _poids<45:
		_reponse=ok
	elif _sexe== "H" and _signe== 3:
		_reponse=ok
	else:
		_reponse=refus
	return _reponse

def auto(_natio,_age,_sexe):
	ok= "Auto : Accessible."
	refus= "Auto : Accès refusé."
	if (_natio== "Italien" or _natio== "Japonais" or _natio=="Allemand") and (89<_age<120) and _sexe=="H":
		 _reponse=ok
	elif _natio=="Autrichien":
		_reponse=ok
	elif _age<17:
		_reponse=ok
	elif _sexe== "F" and 25<_age<35:
		_reponse=ok
	else:
		_reponse=refus
	return _reponse
	
def caroussel(_taille,_age,_sexe):
	ok= "Caroussel : Accessible."
	refus= "Caroussel : Accès refusé."
	if _taille<140 and _age>18:
		_reponse=ok
	elif _sexe=="H":
		_reponse=ok
	else:
		_reponse=refus
	return _reponse

def chaise(_sexe,_age,_taille):
	ok= "Chaises Volantes : Accessible."
	refus= "Chaises volantes : Accès refusé."
	if _sexe=="F" and _age>45:
		_reponse=ok
	elif _taille<150:
		_reponse=ok
	else:
		_reponse=refus
	return _reponse

def trampoline(_sexe,_age,_taille,_poids,_signe):
	ok= "Trampoline de la Reine des Neiges : Accessible."
	refus= "Trampoline de la Reine des Neiges : Accès refusé."
	if _sexe=="H" and _taille>180 and 80<_poids<100 and (_signe== 9 or _signe== 5):
		_reponse=ok
	elif _sexe=="F":
		_reponse=ok
	else:
		_reponse=refus
	return _reponse

def chenille(_natio,_age,_taille):
	ok= "Chenille : Accessible."
	refus= "Chenille : Accès refusé."
	if _natio=="Nigérien" and _age>14 and _taille>150:
		_reponse=ok
	else:
		_reponse=refus
	return _reponse

print("Voici les attractions qui vous sont accessibles ou non selon votre profil:\n")
print(splash(age,signe,sexe,taille))
print(riviere(natio,sexe,age,taille,signe))
print(grandhuit(sexe,age,taille,poids,signe))
print(auto(natio,age,sexe))
print(caroussel(taille,age,sexe))
print(chaise(sexe,age,taille))
print(trampoline(sexe,age,taille,poids,signe))
print(chenille(natio, age, taille))