def Conversion(_prixHT, _devise):
        return round(_prixHT * _devise,2)       

def Tax(_prixConverti, _taxe):
        return round(_prixConverti * _taxe,2) 

def ShowResult(_prixHT, _reduc):
    _euros= 1.0 
    _dollars= 1.19
    _mn= 3395 
    _eurostax= 1.21
    _dollartax= 1.075
    _mntax= 1.10


    print (f"Vous avez choisi une somme de {_prixHT } et une réduction de {_reduc}")
    
    _prixConv= Conversion(_prixHT,_euros)
    _prixTTC= Tax(_prixConv,_eurostax)
    _prixReduc= _prixTTC - _reduc

  
    print("Prix en Euros:")
    print (f"Prix en euros HT : {_prixConv}")
    print (f"Prix en euros TC : {_prixTTC}")
    print(f"Prix total avec réduction : {_prixReduc}")
   
    _prixConv= Conversion(_prixHT,_dollars)
    _prixTTC= Tax(_prixConv, _dollartax)
    _prixReduc=_prixTTC - Conversion(_reduc, _dollars)
   
    print ("Prix en Dollars :")
    print (f"Prix en dollars HT : {_prixConv}")
    print (f"Prix en dollar TC : {_prixTTC}")
    print(f"Prix total avec réduction : {_prixReduc}")

    _prixConv= Conversion(_prixHT,_mn)
    _prixTTC= Tax( _prixConv,_mntax)
    _prixReduc= _prixTTC - (Conversion(_reduc,_mn))
       
    print ("Prix en Tugrik") 
    print (f"Prix en tugrik HT : {_prixConv}")
    print (f"Prix en tugrik TTC : {_prixTTC}")
    print(f"Prix total avec réduction : {_prixConv}")
        




    

ShowResult(float(input("Entrez le prix de votre article sans taxes :\n")),float(input("Entrez la réduction appliquée à votre article en euros :\n")))