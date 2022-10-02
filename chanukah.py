#
# 3
# 1 8   ->  44
# 2 1   ->  2
# 3 10  ->  65

numberOfDataSets = int(input())

dataSets = []

n = 0

while n < numberOfDataSets:
    curI = input().split(" ")
    dataSets.append(int(curI[1]))
    n += 1

print(dataSets)

for i in dataSets:
    print(int(i * ((i + 1) / 2) + i))
