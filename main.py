from postfix import *

print(postfix_eval([3, 4, "+", 5, "*", 6, "-"]))
print(postfix_eval([3, 4, 5, 6, "-", "*", "+"]))
print(postfix_eval("3,4,5,6,-,*,+"))
