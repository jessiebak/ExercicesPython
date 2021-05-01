# Cette fois-ci, toujours à l'aide d'un while, écrivez un programme qui demandera à l'utilisateur de tapper sur une touche
# Si la personne tappe y, le programme s'arrête en disant "vous avez arrêté la boucle prématurément"
# Sinon, le programme continue à poser la question jusque 10x maximum. Après quoi s'arrête sans rien dire.

# Le petit mot "break" permet de sortir d'une boucle quand on le veut

# Résolvez cet exercice une fois avec le mot break et une fois sans utiliseclsr le mot break ! Le programme doit avoir EXACTEMENT
# le même état dans les deux cas. (toutes les valeurs doivent être les mêmes, le résultat le même, etc...)

enter = ""
i = 0
while enter != "y" or  i<10: 
    enter = input("Taper sur n'importe quelle touche du clavier, si vous choisissez 'y' le programme va s'arrêter")
    if enter == "y":
        print("Vous avez arrêté le programme prématurément")
    
    i+=1 
