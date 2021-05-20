# Ecrire TOUT l'alphabet en minuscule et en majuscule à à l'aide d'une boucle for sans utiliser une seule string ou char dans vos variables ! Uniquement des ints !!

for i in range(65,123):
    if 91<= i <= 96:
        continue
    print(chr(i)) 

import string
print(string.ascii_letters)
