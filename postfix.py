#title          :postfix.py
#description    :Calcul d'expressions postfixées simples en python pour le programme de Terminale NSI
#author         :NALIE
#version        :1.0 
#==============================================================================

# -*- coding: utf-8 -*-

from isFunction import *

def postfix_eval(expression): #Prends une expression postfixée et retourne le résultat en float
    if isEmpty(expression): return None #Si l'expression est vide, on ne va pas plus loin

    if isStr(expression): #Convertit le str en list et en fait une copie. Permet de gerer les nombres
        postfix = list(expression.split(",")) 
    else:
        postfix = list(expression) #Expression à calculer, utiliser comme une pile. On copie le tableau pour ne pas le modifier.
    
    postfix = postfix_correct_type(postfix)
    postfixCache = list() #operandCache des nombres à calculer

    while len(postfix) > 1:
        while not isStr(postfix[0]): #On dépile postfix et on empile dans postfixCache jusqu'a arriver à un opérateur
            cache = postfix.pop(0) #depile
            postfixCache.insert(0, cache) #empile

        operand = postfix.pop(0) #On dépile l'opérateur à réaliser dans une variable

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

        postfixCache.pop(0) #On enlève les deux derniers éléments de la pile de operandCache. On vient de les calculer
        postfixCache.pop(0)

    postfix = float(postfix[0]) #On retourne un float. Il ne reste que l'élément 0 dans la pile
    return postfix
    
def postfix_correct_type(postfixExpression):
    postfixCorrect = list()
    for i in postfixExpression: #S'assure du type des elements
        try: #Test si l'élément est un entier, pour l'ajouter en tant que tel dans la liste
            float(i)
            postfixCorrect.append(float(i))
        except ValueError: #Sinon c'est un str
            postfixCorrect.append(i)
    return postfixCorrect


def infix_to_postfix(infix):
    infix = infix.replace(" ", "") #Supprime les espaces si il y en a
    assert isBracketCorrect(infix), "Check bracket in " + str(infix) 
    infix = infix.split(",") #Convertit le str en list. Permet de gerer les nombres

    operandPriority = {"(": 0, ")": 0, "+": 1, "-": 1, "*": 2, "/": 2} #Poids des opérateurs pour les priorités de caculs
    operandCache = list() #Sert de cache pour les operateurs dans l'ordre de priorité
    postfix = list()

    for element in infix:
        if isToken(element): #Si l'element est un nombre ou une lettre, on l'ajoute à l'expression postfixée
            postfix.append(element)
        elif element == "(":
            operandCache.append(element)
        elif element == ")": #Ajoute tout les operateurs dans la parenthèse
            last = operandCache.pop()
            while last != "(":
                postfix.append(last)
                last = operandCache.pop()
        else: #Si l'element est un operateur
            while (not isEmpty(operandCache)) and operandPriority[operandCache[-1]] >= operandPriority[element]: #Si il y a un operateurs dans operandCache et que sa priorité est plus importante que l'element 
                last = operandCache.pop()
                postfix.append(last) #On met l'operateur dans postfix
            
            operandCache.append(element) #on ajoute l'operateur dans le cache

    while not isEmpty(operandCache): #On vide le cache d'operateur dans l'expression
        last = operandCache.pop()
        postfix.append(last)

    postfix = ",".join(postfix) #Retourne une expression plutôt qu'un tableau
    return postfix