import time
import random

# Etape 1 :
for i in range(3):
    print("Hello World")

time.sleep(1)
# Etape 2 :
for i in range(3):
    print("Hello World n°" + str(i))

time.sleep(1)

# Etape 3 :
for i in range(3):
    for j in range(3):
        print((j+1)*".")
        time.sleep(0.3)

time.sleep(1)

# Etape 4  :

for i in range(1, 4):
    for j in range(3):
        print((j+1)*".")
        time.sleep(0.3)

time.sleep(1)

# Etape 5 :

for i in range(3):
    for j in range(1, 20, 2):
        print((j+1)*".")
        time.sleep(0.3)

time.sleep(1)

# Etape 6A :

for i in range(1, 11):
    print("Sending data to server, attempt n°" + str(i))
    time.sleep(0.1)

# Etape 6B:

for i in range(1, 11):
    print("Sending data to server, attempt n°" + str(i))
    time.sleep(0.1)
    if random.random() > 0.9:
        print("Successfuly sent data.")
        break
else:
    print("couldn't send data to serveur, try again.")

# Exemple string :
for i in "Je Suis une Phrase Lambda":
    print(i)
    time.sleep(0.2)
