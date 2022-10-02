"""
3
z -> z -> z
o    z    z
z    o    z



"""
# defines stackHeight as the first line of input
stackHeight = int(input())

# initializes the stack as a list
stack = []

# counter for the bell tolls
bellTolls = 0

zebra_count = 0

# builds the stack of zebras and ocelots from the input in reverse order for easier iteration
for i in range(stackHeight):
    stack.insert(0, input())


def swap_lowest_ocelot(lst):
    for n in lst:
        if n == 'o':
            lowest_ocelot = lst.index(n)
            lst[lowest_ocelot] = 'z'
            for h in lst[:lowest_ocelot]:  # iterates through animals below the lowest ocelot
                if h == 'z':  # checks if the current animal is a zebra
                    lst[lst.index(h)] = 'o'  # turns zebras into ocelots
            break
    return lst


while zebra_count < len(stack):
    zebra_count = 0
    for i in stack:
        if i == 'z':
            zebra_count += 1
    swap_lowest_ocelot(stack)
    bellTolls += 1

print(bellTolls - 1)

