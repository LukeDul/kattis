length = input()
lines = []
for i in range(int(length)):
    pops = list((map(int, input().split(" "))))
    last = 0
    cur = 0
    low_bound = 0
    for j in pops:
        cur = j
        if (((last * 2) < cur) and last != 0):
            low_bound += (cur - 2*last)
        last = cur
    print(low_bound)
