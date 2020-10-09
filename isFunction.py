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

def isStr(a):
    if type(a) == str:
        return True
    else:
        return False

def isBracketCorrect(string): #verifie le bon placement des parenthèses dans une expression type infix
    bracketOpenCount = 0 #Chaque parenthèses ouvrante ajoute 1, chaque fermante retire 1. On doit arriver a 0

    for i in string:
        if i == "(":
            bracketOpenCount += 1
        elif i == ")":
            bracketOpenCount -= 1

    if bracketOpenCount == 0: 
        return True
    else:
        return False