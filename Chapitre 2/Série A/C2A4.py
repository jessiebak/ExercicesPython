# Nous allons coder un programme un peu spécial. c'est une machine à rentrer dans les rêves. 
# Règle à respecter pendant tout le programme :     
# - Notre programme va écrire une phrase toutes les secondes quand c'est à lui de parler 
# (bibliothèque time / fonction time.sleep(secondeEnInt))
# 
# Au début, notre programme va simplement poser la question à l'utilisateur si il désire rentrer dans le rêve d'une personne
# Si l'utilisateur écrit "go", il rentre dans le rêve, sinon, le programme s'arrête et dit à l'utilisateur
# qu'il n'a même pas osé rentrer dans le premier rêve.
# Sinon, c'est là que le fun commence ! Lorsque l'on rentre dans un rêve d'une personne, le temps ralenti et passe
# deux fois plus lentement ! De la, le programme indique à la personne à quel couche de rêve nous nous trouvons
# il dit aussi de combien de fois le temps est ralenti par rapport à la réalité et enfin, dans le rêve de qui nous nous trouvons
# De là, le programme recommence, et nous repropose de rentrer dans le rêve de la personne qui est dans le rêve de la personne ou nous étions à la base !
# Si on accepte, on recommence, le temps est de nouveau 2 fois plus lent qu'avant (4 fois donc), le programme nous dit que
# l'on est à la couche 2 de rêve, que le temps est 4 fois plus lent et que nous nous trouvons dans le rêve
# de la personne qui rêvait, dans le rêve de la personne qui rêvait à la base !
# Un exemple concret, si nous avons été dans le rêve, d'une personne après 4 fois, le programme me dira :
# Vous vous appretez à rentrer dans le rêve d'une personne, attention le temps sera ralenti si vous entre dedans.

# Tappez "go" pour rentrer dans le rêve :
# go
# Bvvvzouit chplklklklk JDONG
# Vous rentrez dans le rêve de la personne, vous êtes à l'étape 4, le temps se ralenti, il est maintenant 16 fois plus lent.
# Vous êtes dans le rêve de la personne
# se trouvant dans le rêve de la personne
# se trouvant dans le rêve de la personne
# se trouvant dans le rêve de la personne
# qui se trouvait devans vous à la base.

# Notez bien que le temps se passe bien 16 fois plus lent, et que donc il y a un délait à ce niveau là de 16 secondes
# entre chaque message que nous envoie le programme !!!!
# A tout moment, on peut décider de s'arrêter de progresser en tappant autre chose que "go" au moment où l'on nous pose la question.
# Si on le fait, le programme nous dit de combien le temps était ralentit là ou nous nous trouvions.
# Exemple :
# Vous vous appretez à rentrer dans le rêve d'une personne, attention le temps sera ralenti si vous entre dedans.
# Tappez "go" pour rentrer dans le rêve :
# kµ
# Vous décidez de ne pas continuer votre chemin, votre voyage s'arrête là. Le temps était 16 fois plus lent là où vous étiez
# C'était sûrement un bon choix de s'arrêter là. Attention, quand on stop la boucle, nous ne sommes pas sorti du rêve,
# le temps reste ralentit. En sortirons-nous un jour ?
# PARTIE 2 : Me prévenir quand vous arrivez là !!! Attendre que tout le monde y soit.
# Si ça vous intéresse, essayez de coder le programme inverse qui s'execute après. On démarre de cet endroit du rêve, et vous proposez
# à l'utilisateur de sortir de ce rêve pour re-rentrer dans celui d'avant, le temps re-avance 2* plus vite et on peut faire ça
# jusqu'à arriver dans la réalité !
import time     

def set_time(_time):
    _time = _time *2
    return _time


i=1
ralentissement = 1
while (i<4):
     
    start = input("Souhaitez vous rentrer dans le rêve d'une personne ? \n Entrez 'go' pour rentrer dans un rêve: \t")
    if start == "go":
        print(f"Vous rentrez dans le rêve n°{i}")
        ralentissement = set_time(ralentissement)
        time.sleep(ralentissement)
        print(f"Le programme ralenti de {ralentissement} secondes")

    i+=1  

    
