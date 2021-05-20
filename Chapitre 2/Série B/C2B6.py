# Demandez une phrase à l'utilisateur, votre programme donnera :
# - Le nombre de majuscule et de minuscule
# - Le nombre d'espace
# - Le nombre de consonnes et de voyelles

from string import ascii_lowercase, ascii_uppercase


phrase= input("Entrez une phrase: \t")

numberspace = phrase.count(" ")
print(numberspace)



