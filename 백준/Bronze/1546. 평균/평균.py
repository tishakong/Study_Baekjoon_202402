N = int(input())
rawScore = input()
newScore = []

rawList = list(map(int,rawScore.split()))

maxScore = max(rawList)

for i in range(len(rawList)):
    newScore.append(rawList[i]/maxScore*100)

print(sum(newScore)/len(newScore))

