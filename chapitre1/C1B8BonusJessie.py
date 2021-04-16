#region ennoncé

# Ennoncé :
# La seule opération se faisant hors des fonction est l'appel de ShowResult() déjà écrit. Cette fonction
# s'occupera exclusivement d'écrire à l'écran le résultat demandé.
# Votre programme devra comme résultat afficher le prix entré par l'utilisateur sans taxe en euro, 
# tugrik(monnaie mongole), et dollars.
# Il devra aussi calculer et montrer le prix avec taxe dans les trois monnaie, et enfin le prix final après
# application de la réduction (c'est une réduction brute pas en %. Si l'utilisateur rentre une réduction 
# de 10 alors ça veut dire qu'on enlève 10 euros au prix final)
# Pas d'indices pour celui-ci autre que le début de code ! Bonne chance !


#Conversion : -USA : 1,19 / -MN : 3395
#TVA : -USA : 7,5% / -EU : 21% / -MN : 10%

#endregion

#region prépa autre

# Préparez aussi : 
# Une petite explication de ce que vous avez fait dans le programme, comment il marche (à expliquer à l'oral 
# à l'autre groupe)
# Une sorte de post mortem. Où on été les difficultés, ce que ça vous a appris, etc. un retour d'expérience,
# pas forcément uniquement sur le code mais aussi potentiellement sur le travail d'équipe, 
# Une explication de ce qu'il faut rajouter à votre programme si je veux simplement ajouter à tout ça un 
# nouveau pays (essayez d'introduire une conversion vers le Metical (monnaie du Mozambique. 
# TVA 17%, taux de change 0,012) ou du moins un explication de comment faire/comment vous avez fait)

# Je pourrais interroger potentiellement n'importe lequel d'entre vous sur chacune de ces questions, 
# je n'ai pas besoin d'un exposé, soyez juste tous pret à y répondre.

#endregion

#region directives

# A 13h30, je vous montrerai le résultat que j'obtient en lançant mon programme pour vous donner une 
# idée de finalité
# Je commencerai à répondre à vos questions seulement après la moité du temps (14H15-14H30). 
# Vous gérez comme vous voulez vos temps de pause, de travail, de reflexion, etc.

# Pendant les quelques dernières minutes de ce cours, si vous n'avez pas fini je m'exprimerai sur des 
# critiques potentielle pour vous aider à le terminer.
# On corrigera tout ça demain en virtuel !

# N'hésitez pas à utiliser internet si besoin, surtout pendant la première phase.
# J'essayerai de vous donner une note pour vos solutions et votre travail, si vous le voulez bien, 
# pas du tout objective ni importante, mais simplement pour vous aider à vous situer par rapport à ce 
# que j'attends de vous à ce stade de ce cours.

#Maximum 2 PC par groupe, 1 seul pour coder ! 
# (l'autre sert pour les recherches internet, consulter l'ennoncé,... uniquement)

#endregion

def ShowResult(_prixHT,_reduc):
    _euros= 1.0 
    _dollars= 1.19
    _mn= 3395 
    _eurostax= 1.21
    _dollartax= 1.075
    _mntax= 1.10


    def conversion(_prixHT, _devise):
        return _prixHT * _devise
        

    def tax(_prixconv,_taxe):
        return _prixconv * _taxe 

    print (f"Vous avez choisi une somme de {_prixHT } et une réduction de {_reduc}")
    
    _prixConv = conversion(_prixHT,_euros)
    _prixTTC=tax(conversion(_prixHT,_euros),_eurostax)
    _prixReduc =  tax(conversion(_prixHT,_euros),_eurostax) - _reduc

    print("Prix en Euros:")
    print (f"Prix en euros HT : {_prixConv}")
    print (f"Prix en euros TC : {_prixTTC}")
    print(f"Prix total avec réduction : {_prixReduc}")
   
    _prixConv =conversion(_prixHT,_dollars)
    _prixTTC=tax(conversion(_prixHT,_dollars),_dollartax)
    _prixReduc =  tax(conversion(_prixHT,_dollars),_eurostax) - conversion(_reduc, _dollars)

   
    print ("Prix en Dollars :")
    print (f"Prix en euros HT : {_prixConv}")
    print (f"Prix en euros TC : {_prixTTC}")
    print(f"Prix total avec réduction : {_prixReduc}")

    _prixConv = conversion(_prixHT,_mn)
    _prixTTC= tax(conversion(_prixHT,_euros),_mntax)
    _prixReduc =  tax(conversion(_prixHT,_euros),_eurostax) - (conversion(_reduc,_mn))
    
    print ("Prix en Tugrik") 
    print (f"Prix en euros HT : {_prixConv}")
    print (f"Prix en euros TTC : {_prixTTC}")
    print(f"Prix total avec réduction : {_prixConv}")
        




    

ShowResult(float(input("Entrez le prix de votre article sans taxes :\n")),float(input("Entrez la réduction appliquée à votre article en euros :\n")))