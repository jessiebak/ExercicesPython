# Enoncé : Ecrivez un programme qui fera office de super calculette ! Le programme demande de rentrer 2 
# chiffres à l'utilisateur, une fois ceux-ci entré, le programme donne le résultat de l'addition,
# la multiplication, la soustraction, la division et le résultat de chacun des nombres mis au carré.
# Chacune des opérations citées doivent se trouver dans une fonction différente.

def Add(_n1,_n2):
    return _n1+ _n2
def Substract(_n1,_n2):
    return  _n1 - _n2
def Multiple(_n1,_n2):
    return  _n1 * _n2
def Division(_n1,_n2):
    return _n1 /_n2
def Square(_n1):
    return _n1*_n1 
def Calculate (_n1,_n2):
    print (f"La somme est {Add(_n1,_n2)}")
    print (f"La soustraction est {Substract(_n1,_n2)}")
    print (f"La multiplication est {Multiple(_n1,_n2)}")
    print (f"La division est {Division(_n1,_n2)}")
    print (f"Le carré de {_n1} est :{Square(_n1)}")
    print (f"Le carré  {_n2} est :{Square(_n2)}")


Calculate(int(input("quel est votre premier nombre")),int(input("Quel est votre deuxième nombre?")))
#region indice
# On peut fonctionner de plusieurs manières pour résoudre cet exercice, essayon déjà de faire une fonction
# qui prend en paramètre 2 variables et qui renvoie le résultat de la somme de ces deux nombres
# Ensuite dans le programme principal on appelle cette fonction pour voir si elle fonctionne
#endregion

#region indice
# Si ça marche, on a juste à recréer 4 autres fonctions pour les 4 autres opérations
#endregion

#region indice
# Pour renvoyer un résultat, on met le petit mot return suivi du résultat. une fonction ne peut renvoyer 
# qu'une seule valeur, pour le carré il faut donc faire appel 2 fois à la même fonction !
#endregion