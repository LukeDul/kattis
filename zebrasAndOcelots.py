"""
3
Z -> Z -> Z
     Z    Z
Z    O    Z

        if n == 'O':
            lowest_ocelot = stack.index(n)
            stack[lowest_ocelot] = 'Z'
O Z O
Z Z O
O O Z
Z O Z
O Z Z
Z Z Z
In terms of Y
Y = 2 * Y(n-1) + 1

In terms of X
Y = x

X -> Y
1 -> 1
2 -> 3
3 -> 7
4 -> 15
5 -> 31
6 -> 63
7 -> 127
8 -> 255

cut off any zs at the top

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


while zebra_count < len(stack):  # O(N^2^2 + N)
    print(stack, bellTolls)

    zebra_count = 0

    for i in stack:  # O(N)
        if i == 'Z':
            zebra_count += 1

    try:
        lowest_ocelot = stack.index('O')
        stack[stack.index('O')] = 'Z'
    except ValueError:
        break

    for h in stack[:lowest_ocelot]:  # O(0-60)
        if h == 'Z':
            stack[stack.index(h)] = 'O'

    bellTolls += 1


# takes too long bruh

