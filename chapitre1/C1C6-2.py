firstPlayerName = input("Entrez le nom de la première personne :\n")
firstPlayerCard = int(input(f"Quelle est le nombre de carte de {firstPlayerName} ? "))
tempPlayernName = input("Entrez le nom de la deuxième personne: \n ")
tempPlayerCard = int(input(f"Quel est le nombre carte de {tempPlayernName} ?")) 

if firstPlayerCard > tempPlayerCard:	
	secondPlayerName = tempPlayernName 
	secondPlayerCard = tempPlayerCard  
else:  
	secondPlayeName = firstPlayerName
	firstPlayerName = tempPlayernName

	secondPlayerCard = firstPlayerCard
	firstPlayerCard = tempPlayerCard 

tempPlayernName = input("Quel est le nom de la troisième personne: \n")
tempPlayerCard = int(input(f"Quel est le nombre de carte {tempPlayernName} ?"))

if secondPlayerCard > tempPlayerCard: 
	thirdPlayerName = tempPlayernName
	thirdPlayerCard = tempPlayerCard

elif tempPlayerCard > firstPlayerCard: 
	thirdPlayerName = secondPlayerName
	thirdPlayerCard = secondPlayerCard
	
	secondPlayeName = firstPlayerName
	secondPlayerCard = firstPlayerCard

	firstPlayerName = tempPlayernName
	firstPlayerCard = tempPlayerCard 
else: 
	thirdPlayerName = secondPlayeName
	thirdPlayerCard = secondPlayerCard

	secondPlayerName = tempPlayernName
	secondPlayerCard = tempPlayerCard

tempPlayernName = input("Quel est le nom de la troisième personne: \n")
tempPlayerCard = int(input(f"Quel est le nombre de carte {tempPlayernName} ?"))

if tempPlayerCard < thirdPlayerCard:
	fourthPlayerName = tempPlayernName
	fourthPlayerCard = tempPlayerCard

elif tempPlayerCard > firstPlayerCard:
	fourthPlayerName = thirdPlayerName
	fourthPlayerCard = thirdPlayerCard

	thirdPlayerName = secondPlayeName
	thirdPlayerCard = secondPlayerCard

	secondPlayeName = firstPlayerName
	secondPlayerCard = firstPlayerCard

	firstPlayerName = tempPlayerName
	firstPlayerCard = tempPlayerCard

elif firstPlayerCard > tempPlayerCard > secondPlayerCard:

	fourthPlayerName = thirdPlayerName
	fourthPlayerCard = thirdPlayerCard

	thirdPlayerName = secondPlayeName
	thirdPlayerCard = secondPlayerCard

	secondPlayeName = tempPlayernName
	secondPlayerCard = tempPlayerCard

else: 
	fourthPlayerName = thirdPlayerName
	fourthPlayerCard = thirdPlayerCard

	thirdPlayerName = tempPlayernName
	thirdPlayerCard = tempPlayerCard


print(f"la première personne est {firstPlayerName} avec {firstPlayerCard} cartes Pokémon")
print(f" La deuxième personne est {secondPlayerName} avec  {secondPlayerCard} cartes Pokémon")
print(f"La troisième personne est {thirdPlayerName} avec {thirdPlayerCard} cartes Pokémon")
print(f"La quatrième personne est {fourthPlayerName} avec  {fourthPlayerCard} cartes Pokémon")

