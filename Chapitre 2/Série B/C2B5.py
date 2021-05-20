# Votre programme demandera à l'utilisateur une lettre (une seule, majuscule ou minuscule). Votre programme dira sa postion dans l'alphabet et si celle-ci est une majuscule ou une minuscule:
# Exemple :
# Vous avez entré la lettre "c", c'est la troisième lettre de l'alphabet et elle est écrite en minuscule.
# Vous avez entré la lettre "B", c'est la deuxième lettre de l'alphabet et elle est écrite en majuscule.

lettre = input("entrez une lettre")
if 65 <= ord(lettre) <= 90: 
    print(f"C'est une lettre majuscule et sa place dans l'alphabet est :{ord(lettre)-64}")
elif 97 <= ord(lettre) <= 122:
    print(f"C'est une lettre minuscule et sa place dans l'alphabet est :{ord(lettre - 96)}")
else: 
    print("C'est un caractère spécial ou inconnu")