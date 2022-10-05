"""
N Teams
M Rooms

Division of teams needs to be ~even

Number, Number, -> Strings
Takes two numbers as input, number of teams and number of rooms,
and outputs a string which indicates the assignments of teams

Input:
1
5
Output:
*****

Input:
3
8
Output:
***
***
**

each num should be max or max - 1




"""


# Float -> Integer
# Rounds float to nearest highest integer
def round_up(num):
    if round(num) < num:
        return round(num) + 1
    else:
        return round(num)


rooms = int(input())
teams = int(input())

max = teams / rooms

print(max)


for i in range(rooms):
    if teams % rooms == 0:
        print('*' * int(max))
    elif:
        print()
        break
