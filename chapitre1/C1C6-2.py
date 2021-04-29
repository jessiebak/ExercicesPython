firstPlayerName = input("Entrez le nom de la première personne :\t")
firstPlayerCard = int(input(f"Quelle est le nombre de carte de {firstPlayerName} ? "))
tempPlayerName = input("Entrez le nom de la deuxième personne: \t ")
tempPlayerCard = int(input(f"Quel est le nombre carte de {tempPlayerName} ?")) 

if firstPlayerCard > tempPlayerCard:	
	secondPlayerName = tempPlayerName 
	secondPlayerCard = tempPlayerCard  
else:  
	secondPlayerName = firstPlayerName
	firstPlayerName = tempPlayerName

	secondPlayerCard = firstPlayerCard
	firstPlayerCard = tempPlayerCard 
#3E Personne 
tempPlayerName = input("Quel est le nom de la troisième personne: \t")
tempPlayerCard = int(input(f"Quel est le nombre de carte {tempPlayerName} ?"))

if secondPlayerCard > tempPlayerCard: 
	thirdPlayerName = tempPlayerName
	thirdPlayerCard = tempPlayerCard

elif tempPlayerCard > firstPlayerCard: 
	thirdPlayerName = secondPlayerName
	thirdPlayerCard = secondPlayerCard
	
	secondPlayerName = firstPlayerName
	secondPlayerCard = firstPlayerCard

	firstPlayerName = tempPlayerName
	firstPlayerCard = tempPlayerCard 
else: 
	thirdPlayerName = secondPlayerName
	thirdPlayerCard = secondPlayerCard

	secondPlayerName = tempPlayerName
	secondPlayerCard = tempPlayerCard
#4E personne 
tempPlayerName = input("Quel est le nom de la quatirème personne: \t")
tempPlayerCard = int(input(f"Quel est le nombre de carte {tempPlayerName} ? \n"))

if tempPlayerCard < thirdPlayerCard:
	fourthPlayerName = tempPlayerName
	fourthPlayerCard = tempPlayerCard

elif tempPlayerCard > firstPlayerCard:
	fourthPlayerName = thirdPlayerName
	fourthPlayerCard = thirdPlayerCard

	thirdPlayerName = secondPlayerName
	thirdPlayerCard = secondPlayerCard

	secondPlayerName = firstPlayerName
	secondPlayerCard = firstPlayerCard

	firstPlayerName = tempPlayerName
	firstPlayerCard = tempPlayerCard

elif firstPlayerCard > tempPlayerCard > secondPlayerCard:

	fourthPlayerName = thirdPlayerName
	fourthPlayerCard = thirdPlayerCard

	thirdPlayerName = secondPlayerName
	thirdPlayerCard = secondPlayerCard

	secondPlayerName = tempPlayerName
	secondPlayerCard = tempPlayerCard

else: 
	fourthPlayerName = thirdPlayerName
	fourthPlayerCard = thirdPlayerCard

	thirdPlayerName = tempPlayerName
	thirdPlayerCard = tempPlayerCard
#5E personne
tempPlayerName = input("Quel est le nom de la cinquième personne: \n")
tempPlayerCard = int(input(f"Quel est le nombre de carte {tempPlayerName} ?"))

if tempPlayerCard < fourthPlayerCard:
	fifthPlayerName = tempPlayerName
	fifthPlayerCard = tempPlayerCard

elif tempPlayerCard > firstPlayerCard:
	fifthPlayerName = fourthPlayerName
	fifthPlayerCard = fourthPlayerCard 

	fourthPlayerName = thirdPlayerName
	fourthPlayerCard = thirdPlayerCard 

	thirdPlayerName = secondPlayerName
	thirdPlayerCard = secondPlayerCard

	secondPlayerName = firstPlayerName
	secondPlayerCard = firstPlayerCard

	fifthPlayerName = tempPlayerName
	firstPlayerCard = tempPlayerCard

elif firstPlayerCard > tempPlayerCard > secondPlayerCard:
	fifthPlayerName = fourthPlayerName
	fifthPlayerCard = fourthPlayerCard 

	fourthPlayerName = thirdPlayerName
	fourthPlayerCard = thirdPlayerCard 

	thirdPlayerName = secondPlayerName
	thirdPlayerCard = secondPlayerCard

	secondPlayerName = tempPlayerName
	secondPlayerCard = tempPlayerCard
elif secondPlayerCard > tempPlayerCard > thirdPlayerCard:

	fifthPlayerName = fourthPlayerName
	fifthPlayerCard = fourthPlayerCard 

	fourthPlayerName = thirdPlayerName
	fourthPlayerCard = thirdPlayerCard 

	thirdPlayerName = tempPlayerName
	thirdPlayerCard = tempPlayerCard

else: 
	fifthPlayerName = fourthPlayerName
	fifthPlayerCard = fourthPlayerCard 

	fourthPlayerName = tempPlayerName
	fourthPlayerCard = tempPlayerCard	





print(f"la première personne est {firstPlayerName} avec {firstPlayerCard} cartes Pokémon")
print(f" La deuxième personne est {secondPlayerName} avec  {secondPlayerCard} cartes Pokémon")
print(f"La troisième personne est {thirdPlayerName} avec {thirdPlayerCard} cartes Pokémon")
print(f"La quatrième personne est {fourthPlayerName} avec  {fourthPlayerCard} cartes Pokémon")
print(f"La cinquième personne est {fifthPlayerName} avec  {fifthPlayerCard} cartes Pokémon")

