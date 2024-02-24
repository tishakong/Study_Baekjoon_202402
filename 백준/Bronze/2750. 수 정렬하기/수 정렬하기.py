N = int(input())
NumList = []

for i in range(N):
    NumList.append(int(input()))

NumList = list(set(NumList))
NumList.sort()

for i in range(len(NumList)):
    print(NumList[i])
