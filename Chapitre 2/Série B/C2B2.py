# Votre programme demandera à l'utilisateur de rentrer une phrase. Si le mot "bordel" y est detecté, il y sera remplacé par une série d'étoile, exemple :
# Entrée utilisateur : J'aime bien manger des pâtes bordel !
# Sortie ordinateur : J'aime bien manger des pâtes ****** !
# Si le mot bordel n'est pas detecté, votre programme dira : "Pas de gros mots détectés"

#  Cherchez par vous même comment remplacer une string et comment détécter une string dans une autre sur internet.

# if var1 in var 2 : 
# var2.replace("")

phrase = input ("Entrez une phrase !")
censure = "bordel"
replacement = "*****"
if censure in phrase:
        phrase = phrase.replace(censure, replacement)
        print(phrase)
else:
    print(phrase)


    