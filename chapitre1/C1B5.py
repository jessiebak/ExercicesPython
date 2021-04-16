# Enoncé : Créez d'abord 2 fonctions. Une qui va écrire l'âge, et une qui va écrire la date de naissance
#1# (avec une petite phrase qui accompagne du style "Vous avez X ans")
# de la personne qui appelle la fonction. La première fonction prend en paramètre l'âge, la deuxième prend
# en paramètre la date de naissance en chaîne de caractère.
# Appelez ces deux fonctions pour que cela affiche d'abord l'âge puis la date de naissance de la personne

# Maintenant le réel exercice Au seul appel d'une fonction (vous pouvez en recréer si vous voulez), l'âge 
# Et la date de naissance de la personne seront affichés. Il y a trois solutions possibles, essayez de les
# trouver !
def Tellage(_age):
    print(f"Vous avez {_age}")
def Telldate(_date):
    print(f"Vous êtes né en {_date}")


def TellBoth(_age, _birthyear):
    Tellage(_age)
    Telldate(_birthyear)

TellBoth(23,1995)


    

#1



def user_age_and_date(_age):
    _currentYear = 2021
    print (f"Bonjour, vous avez {_age} ans et êtes né en {_currentYear - _age}")





    
TellBoth(2,1995)


#region indice
# La première est la plus simple, il suffit dans cette fonction de réécrire ce qu'il se passe dans les
# deux fonctions précédentes, c'est la plus "mauvaise" solution. Dans l'absolu, mais la meilleur dans ce cas
#endregion

#region indice
# La deuxième solution est, depuis cette troisième fonction, d'appeler les deux autres fonctions,
# C'est la solution la plus classique et la meilleure
#endregion

#region indice
# La troisème solution est de faire en sorte que depuis la première fonction, on appelle la deuxième
#endregion