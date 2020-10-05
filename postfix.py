#title          :postfix.py
#description    :Calcul d'expressions postfixées simples en python pour le programme de Terminale NSI
#author         :NALIE
#version        :1.0 
#==============================================================================

# -*- coding: utf-8 -*-
#[3, 4, 5, 6, "-", "*", "+"] = 7   [3, 4, "+", 5, "*", 6, "-"] = -29

def strToPostfix(string):
    string = list(string)
    postfixExpression = []
    for i in string:
        try:
            int(i)
            postfixExpression.append(int(i))
        except ValueError:
            postfixExpression.append(i)

    return postfixExpression


def postfixe_eval(expression):
    if len(expression) == 0: return None #Si l'expression est vide, on ne va pas plus loin

    if(type(expression) == str): expression = strToPostfix(expression) #Si c'est un str on le convertit en array

    postfixe = list(expression) #Expression à calculer, utiliser comme une pile. On copie le tableau.
    postfixeCache = list() #Cache des nombres à calculer

    while len(postfixe) > 1:
        while type(postfixe[0]) != str: #On dépile postfixe et on empile de postfixeCache 
            postfixeCache.insert(0, postfixe[0])
            postfixe.pop(0)

        operand = postfixe[0] #On dépile l'opérateur à réaliser dans une variable
        postfixe.pop(0)

        #On calcul et on empile dans postfixe
        if operand == "+":
            postfixe.insert(0, postfixeCache[0] + postfixeCache[1])
        elif operand == "-":
            postfixe.insert(0, postfixeCache[0] - postfixeCache[1])
        elif operand == "*":
            postfixe.insert(0, postfixeCache[0] * postfixeCache[1])
        elif operand == "/":
            postfixe.insert(0, postfixeCache[0] / postfixeCache[1])
        else:
            assert False, "Opérateur " + str(operand) +  " inconnu"

        postfixeCache.pop(0) #On enlève les deux derniers éléments de la pile de cache. On vient de les calculer
        postfixeCache.pop(0)

    postfixe = int(postfixe[0])
    return postfixe

print(postfixe_eval([3, 4, "+", 5, "*", 6, "-"]))
print(postfixe_eval([3, 4, 5, 6, "-", "*", "+"]))
print(postfixe_eval("3456-*+"))