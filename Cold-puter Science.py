# SOLVED

n = int(input())

my_list = input().split()

counter = 0

for i in my_list:
    if int(i) < 0:
        counter += 1

print(counter)
