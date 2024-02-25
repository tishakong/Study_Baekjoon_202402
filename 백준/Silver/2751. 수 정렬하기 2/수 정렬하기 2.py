import sys

N = int(sys.stdin.readline())
NumList = [0 for i in range(N)]

for i in range(N):
    NumList[i]=int(sys.stdin.readline())

NumList = list(set(NumList))
NumList.sort()

for i in range(len(NumList)):
    print(NumList[i])
