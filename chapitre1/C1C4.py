# Enoncé : Vous créez une petie application qui donne les horaires des trains. L'utilisateur choisira sa destination et la période à laquelle il veut partir et votre application
# donnera l'heure du train. Concrètement le résultat devra ressembler à ceci :

# 1 - Bruxelles
# 2 - Mons
# 3 - Nivelles
# 4 - Charleroi
# Entrez La destination que vous voulez atteindre : 3
# Bien, vous avez choisi d'aller à Nivelles.
# 1 - Matin
# 2 - Après-midi
# 3 - Soir
# Quand souhaitez vous partir ? 3
# Ok, vous avez choisi la période : Soir
# Votre train démarre à 20h00

# Les heures sont les suivantes :
# Bruxelles (Matin) : 10h33
# Bruxelles (Midi) : 14h42
# Bruxelles (Soir) : 19h02

# Mons (Matin) : 9h10
# Mons (Midi) : 13h30
# Mons (Soir) : 22h56

# Nivelles (Matin) : 5h34
# Nivelles (Midi) : 15h13
# Nivelles (Soir) : 20h00

# Charleroi (Matin) : 7h45
# Charleroi (Midi) : 12h53
# Charleroi  (Soir) : 23h02
import sys

def ChooseDestination():
    print("Bienvenue sur l'application des trains. ")
    print("Les destinations disponibles sont: \n 1. Bruxelles \n 2. Mons \n 3. Nivelles \n 4. Charleroi \n ")
    _destinationChoice = int(input("Entrez votre destination : \n"))
    if _destinationChoice == 1: 
        _destination = "Bruxelles"
    elif _destinationChoice == 2: 
        _destination = "Mons"
    elif _destinationChoice == 3: 
        _destination = "Nivelles"
    elif _destinationChoice == 4: 
        _destination = "Charleroi"
    else:
        sys.exit("Erreur la destination entrée est incorrecte")
    
    print(f"Bien vous avez décidé d'aller à {_destination}\n")


    return _destination

def ChoosePeriod():
    print("Les périodes disponibles : \n 1. Matin \n 2. Midi \n 3. Soir")
    _periodChoice = int(input("Quand souhaitez-vous partir"))

    if _periodChoice == 1:
        _period = "Matin"
    elif _periodChoice == 2:
        _period = "Midi"
    elif _periodChoice == 3:
        _period = "Soir"
    else:
        sys.exit("Erreur la période est incorrecte")
    
    print(f"Vous aves choisi la péride :{_period}")
    return _period    

def DisplayTime(_time,_morningHour, _afternoonHour,_eveningHour):
    if _time == "Matin":
        print(f"Votre train arrive à : {_morningHour}")
    elif _time == "Midi":
        print(f"Votre train arrive à :{_afternoonHour}")
    elif _time == "Soir":
        print(f"Votre train arrive à :{_eveningHour}")

   

destination = ChooseDestination()
period = ChoosePeriod()



if destination == "Bruxelles":
    DisplayTime(period, "10h33", "14h42", "19h02")
elif destination == "Mons":
    DisplayTime(period, "9h10", "13h30", "22h56")
elif destination == "Nivelles":
    DisplayTime(period, "5h34", "15h13", "20h20")
elif destination == "Charleroi":
    DisplayTime(period, "7h43", "12h53", "23h02")



    
    