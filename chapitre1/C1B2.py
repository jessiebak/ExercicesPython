# Enoncé : Créez une fonction qui va dire bonjour à quelqu'un. Elle a un paramètre, le nom de la personne
# que le programme salue.
#  Essayez d'appeler la fonction de 4 manières différentes 
# et une fois avec un input 
#  stocké dans une variable.

def bonjour (_name):
    print (f"Bonjour à toi {_name}") 


#1er 
bonjour("Mattéo")

#2
prenom = "lucas"
bonjour(prenom)

#3
bonjour(input("Quel est votre prénom? \n "))

#4
prenom = input("Quel est votre prénom? \n")
bonjour(prenom)



#region indice
# 1) avec une string directement.
#endregion

#region indice
# 2) Avec une variable qui stocke une string
#endregion

#region indice
# 3) Avec un input direct à l'appel de la fonction
#endregion

#region indicec
# 4) Avec le resultat d'un input stocké dans une variable 
#endregion