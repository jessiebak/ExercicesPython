# Enoncé : Créez une fonction IDCard. Elle prend 3 variables en paramètre. Elles représentent dans l'ordre
#  Le nom, l'   et le sexe de la personne qui va appeler la fonction. Appelez cette fonction de
# deux façons différentes. la première fois vous donnerez le nom, l'âge et le sexe dans le bon
# ordre, la deuxième fois, vous essayerez de donner les paramètres dans un ordre différent, pour autant
# la fonction doit marcher de la même manière !

def IDCard(_name,_age,_sex):

    print(f"Prénom :{_name}")
    print(f"Âge : {_age}")
    print(f"Sexe : {_sex}\n")

#appel même ordre
IDCard("Jessie",25, "M")

IDCard(_sex="M", _age=25,_name="Jessie")

#region indice
# Pour déclarer plusieurs paramètres, séparez lez d'une virgule
#endregion

#region indice
# Il en va de même pour l'appel de la fonction, on sépare les paramètres d'une virgule
#endregion

#region indice
# Pour donner les paramètres dans un ordre différent de la déclaration, on les nommes à l'appel
# de la fonction suivi d'un egal, avant d'enfin donner une valeur.
#endregion