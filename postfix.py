#Calcul d'expressions postfixées simples en python pour le programme de Terminale NSI
#[3, 4, 5, 6, "-", "*", "+"] = 7   [3, 4, "+", 5, "*", 6, "-"] = -29


postfixe = [3, 4, 5, 6, "-", "*", "+"] #Expression à calculer, utiliser comme une pile
postfixeCache = [] #Cache des nombres à calculer
i = 0 #i reste à 0, on utilise ici une pile. On supprime en dépilant

while len(postfixe) > 1:
    while type(postfixe[i]) != str: #On dépile postfixe et on empile de postfixeCache 
        postfixeCache.insert(0, postfixe[i])
        postfixe.pop(i)

    expression = postfixe[i] #On dépile le calcul à réaliser dans une variable
    postfixe.pop(i)


    #On calcul et on empile dans postfixe
    if expression == "+":
        postfixe.insert(0, postfixeCache[0] + postfixeCache[1])
    elif expression == "-":
        postfixe.insert(0, postfixeCache[0] - postfixeCache[1])
    elif expression == "*":
        postfixe.insert(0, postfixeCache[0] * postfixeCache[1])
    elif expression == "/":
        postfixe.insert(0, postfixeCache[0] / postfixeCache[1])

    postfixeCache.pop(0) #On vide la pile de cache
    postfixeCache.pop(0)


print(postfixe)