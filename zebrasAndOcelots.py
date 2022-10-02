"""
3
Z -> Z -> Z
    Z    Z
Z    O    Z



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
        if n == 'O':
            lowest_ocelot = lst.index(n)
            lst[lowest_ocelot] = 'Z'
            for h in lst[:lowest_ocelot]:  # iterates through animals below the lowest ocelot
                if h == 'Z':  # checks if the current animal is a zebra
                    lst[lst.index(h)] = 'O'  # turns zebras into ocelots
            break
    return lst


while zebra_count < len(stack):
    zebra_count = 0
    for i in stack:
        if i == 'Z':
            zebra_count += 1
    swap_lowest_ocelot(stack)
    bellTolls += 1

print(bellTolls - 1)

# takes too long bruh

