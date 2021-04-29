# Nous allons parcourir ce code au cours. La mission du chapitre 2 sera De nous permettre d'utiliser ce genre d'outils, et surtout vous donner la possibilité d'améliorer ce programme !

# 0) Essayer d'expliquer le fonctionnement du programme
# 1) Ajoutons le fait de renvoyer un message d'erreur lors d'une division par 0
# 2) Rajoutons l'opération exposant (_x ** _y)
# 3) Ajoutons un petit chiffre au début de la boucle qui dit à combien de tour on est

def Add(_x, _y):
    return _x + _y


def Subtract(_x, _y):
    return _x - _y


def Multiply(_x, _y):
    return _x * _y


def Divide(_x, _y):
	return _x/_y

def Exp(_x, _y):
	return x ** y 



def Calculate(_operator, _x, _y):
    cases = {
        "+": Add,
        "-": Subtract,
        "*": Multiply,
        "/": Divide,
		"**": Exp
    }
    return cases[_operator](_x, _y)

i= 1
while True:
	print(f"Execution n°{i} du programme")
	if("y" != input("Si vous souhaitez faire une opération, entrez \"y\", toute autre entrée quittera le programme.\n")):
	    print("Bonne journée")
	    break
	x = float(input("Entrez le premier nombre de votre opération\n"))
	y = float(input("Entrez le deuxième nombre de votre opération\n"))
	operator = input("Quelle opération souhaitez vous faire entre ces 2 nombres ?\n1) Tapper \"+\" pour une addition\n1) Tapper \"-\" pour une soustraction\n1) Tapper \"/\" pour une division\n1) Tapper \"*\" pour une multiplication\n 1) taper \"**\" pour exposant\n ")
	i+=1
	try:
		print(Calculate(operator, x, y))
	except ZeroDivisionError:
		print("Erreur ! Vous ne pouvez pas diviser par zéro!")