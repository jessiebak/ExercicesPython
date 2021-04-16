# En sachant que les fréquences des notes suivantes :
# Do = 130
# Ré = 146
# Mi = 164
# Fa = 174
# Sol = 196
# La = 220
# Si = 246
# Sol (grave) = 98
# Essayez de reproduire frère jacques avec la fonction winsound.Beep(), Les notes composants frères jacques sont:
# Do Ré Mi Do Do Ré Mi Do Mi Fa Sol Mi Fa Sol Sol la Sol Fa Mi Do Sol La Sol Fa Mi Do Do Sol(grave) Do Do Sol(grave) Do
# Pour faire un silence, utilisez la fréquence la plus basse possible de la fonction Beep, essayez de régler
# la durée des notes pour que ça sonne le mieux ! (Si vous vous connaissez en musique, n'hésitez pas à 
# réaliser une autre musique à la place de frère jacques !)

import winsound

  
blanche = 1000
noire = 500
croche = 250
double_croche= 125
do, re, mi, fa, sol, la, si, sol2 = 130, 146, 164, 174, 195, 220, 246, 96

frere_jacques = []
douce_nuit = []

frere_jacques = [do, re, mi, do, do, re, mi, do, mi, fa, sol, mi, fa, sol, sol, la, sol, fa, mi, do, sol, la, sol, fa, mi, do, do,sol2, do, do, sol2,do]
douce_nuit = [sol, la, sol, mi, sol, la, sol, mi, re, re, si, do, do, sol, la , la, do, si, la, sol, la, sol, mi,la, la, do, si, la, sol, la, sol, mi, re, re, fa, re, si,do, mi, do, sol, mi, sol, fa, re,do]


duration= []
duratio1 = [noire, noire, noire, noire,noire, noire, noire, noire, noire,noire, blanche, noire, noire, blanche, croche, croche, croche, croche, noire, noire, croche, croche, croche, croche, noire, noire, noire, noire, blanche, noire, noire, blanche]
duration2 = [blanche, noire, blanche, blanche,blanche, noire, blanche, blanche,blanche, noire, blanche, blanche, noire, blanche, blanche, noire, blanche, croche, noire, blanche, croche, noire, blanche, blanche, noire, blanche, croche, noire, blanche, croche, noire, blanche, blanche, noire, blanche, double_croche, noire, blanche, blanche, noire, noire, noire, blanche, double_croche, noire, blanche]
run = 1
run = bool(run)

while (run):
    choice = input("quelle musique souhaitez-vous entendere ? \n 1. Frères Jacques, 2. Douce nuit")

    choice = int(choice)

    if choice == 1:
        melody = frere_jacques
        duration = duratio1
        run = 0
    elif choice == 2:
        melody = douce_nuit
        duration = duration2
        run = 0
    else : 
        print("Votre entrée n'est pas valide")
 



i = 0 
for item in melody:

    winsound.Beep(item,duration[i])
    i+= 1
