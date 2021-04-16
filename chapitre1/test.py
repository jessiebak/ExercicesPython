
from random import shuffle #j'importe la fonction de mélange

names = ["Mahsum", "Jessie", "Eleonor","Maxime", "Bruno", "Alain","Isaac"] #je crée une liste qui contient les noms
total_questions = 20 #je précise le nombre de questions du quizz
print(names)

shuffle(names) #je mélange une première fois la liste
questions = range(total_questions) #je passe dans la variable question, le nombre de fois où il faudra afficher un nom, en fonction du nombre de questions
i = 0 #j'initialise le compteur d'index pour qu'il parcours tous les noms de 0 à len()-1
for number, item in enumerate(questions): #je crée ma boucle for avec un compteur (numberà, pour chaque élément de la liste questions)
    print(number+1, names[i]) #j'écris le numéro de la question, et le nom assiocié
    i+=1   
    if i == (len(names)): #pour ne pas dépasser le taille de la liste, un fois arrivé au dernier nom de la liste on la remélange et on recommence à 0
        shuffle(names)
        i=0


    