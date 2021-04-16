def ShowResult(money, reduction):
    print("Prix en euros: ")
    calc(money, reduction, 0.21)
    print("Prix en dollars: ")
    calc(money*1.19, reduction*1.19, 0.075)
    print("prix en Tugrik: ")
    calc(money*3395, reduction*3395, 0.1)
def calc(money, reduction, TVA):
    brut= money+money*TVA
    reduit= brut- reduction
    print("Prix hors TVA: " + str(money))
    print("Prix avec TVA: " + str(brut))
    print("Prix réduit : " + str(reduit))
ShowResult(float(input("Entrez le prix de votre article sans taxes :\n")),float(input("Entrez la réduction appliquée à votre article en euros :\n")))
#Faire une fonction pour chaque calcul? = plus facile de changer dans une fonction (transformer variable "reduit et brut" en fonctions)