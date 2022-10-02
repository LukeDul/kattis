"""
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
# List -> Number
#
def count_tolls (lst):
    for char in lst:
        if char == 'O':

    len(lst)

def uniform_list (lst):
    if len(lst) == 0:
        return True
    else:
        for b in range(len(lst)):
            if lst[b] == lst[b - 1]

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

    zebra_count = 0

    for i in stack:  # O(N)  0-60
        if i == 'Z':
            zebra_count += 1

    try:
        lowest_ocelot = stack.index('O')  # O(N) 0-60
        stack[stack.index('O')] = 'Z'     # O(N) 0-60
    except ValueError:
        break

    for c in stack[:lowest_ocelot]:  # O(N)  0-60
        if c == 'Z':
            stack[stack.index(h)] = 'O'

    bellTolls += 1

print(bellTolls)
