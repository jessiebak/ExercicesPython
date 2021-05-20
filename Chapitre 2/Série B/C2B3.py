# Créez un programme qui zozotte !
# Votre programme demandera une phrase à l'utilisateur
# Votre programme remplacera tous les "j" et les "ch" par des "z" et ensuite affichera cette phrase transformée

phrase = input("Entrez une phrase")

phrase = phrase.replace("j", "z")
phrase = phrase.replace("ch", "z")
phrase = phrase.replace("J", "Z")
phrase = phrase.replace("Ch", "Z")

print(phrase)

