"""

input: 
 ho|lo
 pe|ve

 output: 
 hope love 

"""

substring1, substring2 = input().split("|")
substring3, substring4 = input().split("|")

print(substring1 + substring3 + " " + substring2 + substring4)
