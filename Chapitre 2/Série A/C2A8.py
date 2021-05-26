# Notre programme simulera la prise d'une potion d'un personnage de jeu vidéo.
# la potion régénère 1 point de vie par secondes pendant 10 secondes ! (time.sleep)
# A chaque fois que le personnage récupère un point de vie, le programme le dit.
# Si le personnage réussi à récupérer tous ses points de vies (20), le programme s'arrête et dit
# Que le personnage a récupéré tous ses points de vies.
# Si et seulement SI le personnage n'a pas récupéré tous les points de vie au bout de 10 secondes, le programme
# Indique à l'utilisateur combien son personnage a maintenant de point de vie.

# Un else qui suit un while permet d'executer un bout de code uniquement si la condition évaluée par le while 
# passe à false ! Si on sort d'un while par un un break, le code dans le else ne S'EXECUTE PAS !!!
# Ecrivez ce programme à l'aide d'un while else et sans l'aide de celui-ci ! 

# Exemple 1 : PDV de départ 6 
# Votre potion vous fait récupérer 1 point de vie
# Votre potion vous fait récupérer 1 point de vie
# Votre potion vous fait récupérer 1 point de vie
# Votre potion vous fait récupérer 1 point de vie
# Votre potion vous fait récupérer 1 point de vie
# Votre potion vous fait récupérer 1 point de vie
# Votre potion vous fait récupérer 1 point de vie
# Votre potion vous fait récupérer 1 point de vie
# Votre potion vous fait récupérer 1 point de vie
# Votre potion vous fait récupérer 1 point de vie
# Vous avez maintenant 16 points de vie

# Exemple 2 : PDV de départ 16 
# Votre potion vous fait récupérer 1 point de vie
# Votre potion vous fait récupérer 1 point de vie
# Votre potion vous fait récupérer 1 point de vie
# Votre potion vous fait récupérer 1 point de vie
# Vous avez maintenant toute votre vie

import time


i = 0
PV = 4
FullPV = 20 
Maxtime = 10 

print(f"Points de vie de départ :{PV}")
while (i < Maxtime and PV <= FullPV): 
    time.sleep(1)
    print("votre potion vous fait récupérer 1 point de vie")
    PV+=1 
    i+=1
else: 
    if PV >= FullPV:
        print("Vous avez récupéré tous vos points de vie")
    else: 
        print(f"Vous avez récupéré seulement {PV} points de vie")

