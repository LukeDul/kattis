#
# 3
# 1 8   ->  44
# 2 1   ->  2
# 3 10  ->  65

numberOfDataSets = int(input())

dataSets = []

for i in range(0, numberOfDataSets):
    currentInput = input().split(" ")
    dataSets.append(currentInput)

for i in dataSets:
    print(i[0], end=" ")
    print(int(int(i[1]) * ((int(i[1]) + 1) / 2) + int(i[1])))
