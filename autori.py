# COMPLETE

# The first and only line of input will contain at most 100
# characters, uppercase and lowercase letters of the English alphabet and hyphen (‘-’ ASCII45).
# The first character will always be an uppercase letter.
# Hyphens will always be followed by an uppercase letter.
# All other characters will be lowercase letters.

# String -> String
# Input: Knuth-Morris-Pratt Output: KMP
x = input()

printNext = False

print(x[0], end="")
for i in x:
    if printNext:
        print(i, end="")
        printNext = False
    elif i == "-":
        printNext = True
