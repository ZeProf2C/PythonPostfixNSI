#[3, 4, 5, 6, "-", "*", "+"] = 7   [3, 4, "+", 5, "*", 6, "-"] = -29

from postfix import *

print(postfix_eval([3, 4, "+", 5, "*", 6, "-"]))
print(postfix_eval([3, 4, 5, 6, "-", "*", "+"]))
print(postfix_eval("3,4,5,6,-,*,+"))

print(infix_to_postfix("22,+,4,*,3"))