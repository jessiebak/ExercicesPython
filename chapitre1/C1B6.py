# Enoncé : Créez une fonction qui va avoir 2 paramètre. Ces deux paramètres sont des chiffres
# représentant l'âge de deux personnes. Cette fonction écrira une petite phrase du style 
# "l'age de la personne 1 est... l'âge de la personne deux est ..."
# la deuxième utilité de cette fonction est de calculer la somme de ces âges. La fonction
# renverra le résultat au programme principal qui lui devra afficher une phrase du style
# "la somme des deux âges vaut ..."


  


#region indice
# N'oubliez pas de transformer vos chiffres en string à l'aide du constructeur string() quand vous voulez
# les afficher
#endregion

#region indice
# Pour renvoyer une valeur au programme principal, utilisez le petit mot clef return
#endregion

#region indice  
# exemple :
# def Function(_nbr1,_nbr2)
#   _sum=_nbr1+_nbr2
#   return sum
# print(Function(1,5))
# ce petit code écrira 6
#endregion

def ageAddition(_age1,_age2):
    
    print("La personne 1 a "+ str(_age1))
    print("La personne 2 a " + str(_age2))
    _sum = _age1 +_age2
    return _sum 

print("La somme des âges est :"+ str(ageAddition(23,25)))
