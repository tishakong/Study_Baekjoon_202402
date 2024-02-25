import sys

n = int(sys.stdin.readline())


if n==0:
    print(0)
else:
    answer = [0 for i in range(n)]
    for i in range(n):
        answer[i]=int(sys.stdin.readline())

    answer.sort()

    filtercnt=int(n*0.15+0.5)

    if filtercnt==0:
        
        print(int(sum(answer)/len(answer)+0.5))
    else:
        filterdList=answer[filtercnt:-(filtercnt)]
        print(int(sum(filterdList)/len(filterdList)+0.5))
