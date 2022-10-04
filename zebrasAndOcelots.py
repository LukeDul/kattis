# COMPLETE
# defines stackHeight as the first line of input Z Z 0 Z 0
stackHeight = int(input())

# initializes the stack as a list
stack = []

# builds the stack of zebras and ocelots from the input in reverse order for easier iteration
for i in range(stackHeight):
    stack.insert(0, input())

summation = 0

for i in range(len(stack)):
    if stack[i] == 'O':
        tolls = 2**i
        summation = tolls + summationg
print(summation)
