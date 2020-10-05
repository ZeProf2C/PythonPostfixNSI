#title          :postfix.py
#description    :Calcul d'expressions postfixées simples en python pour le programme de Terminale NSI
#author         :NALIE
#version        :1.0 
#==============================================================================

# -*- coding: utf-8 -*-
#[3, 4, 5, 6, "-", "*", "+"] = 7   [3, 4, "+", 5, "*", 6, "-"] = -29

def str_to_postfix(string):
    string = list(string)
    postfixExpression = []
    for i in string:
        try: #Test si l'élément est un entier, pour l'ajouter en tant que tel dans la liste
            int(i)
            postfixExpression.append(int(i))
        except ValueError:
            postfixExpression.append(i)

    return postfixExpression


def postfix_eval(expression):
    if len(expression) == 0: return None #Si l'expression est vide, on ne va pas plus loin

    if(type(expression) == str): expression = str_to_postfix(expression) #Si c'est un str on le convertit en liste

    postfix = list(expression) #Expression à calculer, utiliser comme une pile. On copie le tableau pour ne pas le modifier.
    postfixCache = list() #Cache des nombres à calculer

    while len(postfix) > 1:
        while type(postfix[0]) != str: #On dépile postfix et on empile de postfixCache jusqu'a arriver à un opérateur
            postfixCache.insert(0, postfix[0])
            postfix.pop(0)

        operand = postfix[0] #On dépile l'opérateur à réaliser dans une variable
        postfix.pop(0)

        #On calcul et on empile dans postfix
        if operand == "+":
            postfix.insert(0, postfixCache[0] + postfixCache[1])
        elif operand == "-":
            postfix.insert(0, postfixCache[0] - postfixCache[1])
        elif operand == "*":
            postfix.insert(0, postfixCache[0] * postfixCache[1])
        elif operand == "/":
            postfix.insert(0, postfixCache[0] / postfixCache[1])
        else:
            assert False, "Opérateur " + str(operand) +  " inconnu" 

        postfixCache.pop(0) #On enlève les deux derniers éléments de la pile de cache. On vient de les calculer
        postfixCache.pop(0)

    postfix = int(postfix[0]) #On retourne un entier. Il ne reste que l'élément 0 dans la pile
    return postfix