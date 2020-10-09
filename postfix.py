#title          :postfix.py
#description    :Calcul d'expressions postfixées simples en python pour le programme de Terminale NSI
#author         :NALIE
#version        :1.0 
#==============================================================================

# -*- coding: utf-8 -*-

def str_to_expression(string): #prend un str sous forme 2,+,13 pour en faire un tableau avec des bons type
    string = string.split(",")
    postfixExpression = list()
    for i in string:
        try: #Test si l'élément est un entier, pour l'ajouter en tant que tel dans la liste
            float(i)
            postfixExpression.append(float(i))
        except ValueError: #Sinon c'est un str
            postfixExpression.append(i)
    return postfixExpression


def postfix_eval(expression): #Prends une expression postfixée et retourne le résultat en float
    if len(expression) == 0: return None #Si l'expression est vide, on ne va pas plus loin

    if(type(expression) == str): expression = str_to_expression(expression) #Si c'est un str on le convertit en liste

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

    postfix = float(postfix[0]) #On retourne un float. Il ne reste que l'élément 0 dans la pile
    return postfix
    

def infix_to_postfix(infix):
    infix = infix.replace(" ", "") #Supprime les espaces si il y en a
    assert isBracketCorrect(infix), print(isBracketCorrect(infix)) 
    infix = infix.split(",") #Convertit le str en list. Permet de gerer les nombres

    operandPriority = {"(": 0, ")": 0, "+": 1, "-": 1, "*": 2, "/": 2} #Poids des opérateurs pour les priorités de caculs
    postfix = list()
    cache = list() #Sert de cache pour les operateurs dans l'ordre de priorité

    for element in infix:
        print(element)
        if isToken(element): #Si l'element est un nombre ou une lettre, on l'ajoute à l'expression postfixée
            postfix.append(element)
        elif element == "(":
            cache.append(element)
        elif element == ")": #Ajoute tout les operateurs dans la parenthèse
            last = cache.pop()
            while last != "(":
                postfix.append(last)
                last = cache.pop()
        else: #Si l'element est un operateur
            while (not isEmpty(cache)) and operandPriority[cache[-1]] >= operandPriority[element]: #Si il y a un operateurs dans cache et que sa priorité est plus importante que l'element 
                last = cache.pop()
                postfix.append(last) #On met l'operateur dans postfix
            
            cache.append(element) #on ajoute l'operateur dans le cache

    while not isEmpty(cache): #On vide le cache d'operateur dans l'expression
        last = cache.pop()
        postfix.append(last)

    postfix = ",".join(postfix) #Retourne une expression plutôt qu'un tableau
    return postfix


def isToken(char):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if char in letters.upper() or char in letters.lower() or char.isnumeric():
        return True
    else:
        return False

def isEmpty(a):
    if len(a) > 0:
        return False
    else:
        return True

def isBracketCorrect(string): #verifie le bon placement des parenthèses dans une expression type unfix
    bracketOpenCount = 0 #Chaque parenthèses ouvrante ajoute 1, chaque fermante retire 1

    for i in string:
        if i == "(":
            bracketOpenCount += 1
        elif i == ")":
            bracketOpenCount -= 1

    if bracketOpenCount == 0: 
        return True
    else:
        return False