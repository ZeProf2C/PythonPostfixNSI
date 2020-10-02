#Calcul d'expressions postfixées simples en python pour le programme de Terminale NSI
#[3, 4, 5, 6, "-", "*", "+"] = 7   [3, 4, "+", 5, "*", 6, "-"] = -29


postfixe = [3, 4, 5, 6, "-", "*", "+"] #Expression à calculer, utiliser comme une pile
postfixeCache = [] #Cache des nombres à calculer

while len(postfixe) > 1:
    while type(postfixe[0]) != str: #On dépile postfixe et on empile de postfixeCache 
        postfixeCache.insert(0, postfixe[0])
        postfixe.pop(0)

    expression = postfixe[0] #On dépile le calcul à réaliser dans une variable
    postfixe.pop(0)


    #On calcul et on empile dans postfixe
    if expression == "+":
        postfixe.insert(0, postfixeCache[0] + postfixeCache[1])
    elif expression == "-":
        postfixe.insert(0, postfixeCache[0] - postfixeCache[1])
    elif expression == "*":
        postfixe.insert(0, postfixeCache[0] * postfixeCache[1])
    elif expression == "/":
        postfixe.insert(0, postfixeCache[0] / postfixeCache[1])

    postfixeCache.pop(0) #On enlève les deux derniers éléments de la pile de cache. On vient de les calculer
    postfixeCache.pop(0)


print(postfixe)